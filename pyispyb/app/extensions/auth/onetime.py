import logging
import secrets
from typing import Optional
from urllib.parse import urlparse

from fastapi import Query, HTTPException
from ispyb import models
from sqlalchemy import text

from ....config import settings
from ...extensions.database.definitions import get_current_person
from ...extensions.database.middleware import db

logger = logging.getLogger(__name__)


def onetime(
    onetime: Optional[str] = Query(
        None,
        description="One time token",
        include_in_schema=False,
        regex=r"^([\w\-_])+$",
    )
) -> str:
    return onetime


def generate_onetime_token(validity: str, personId: int) -> str:
    """Generate a one time token

    Kwargs:
        validity (str): The path this token is valid for
        login (str): The associated person login

    Returns:
        token(str): The generated token
    """
    parsed = urlparse(validity)
    path = parsed.path
    path = path.replace(settings.api_root, "")

    token = secrets.token_urlsafe(96)
    once_token = models.SWOnceToken(
        personId=personId,
        validity=path,
        token=token,
    )
    db.session.add(once_token)
    return token


def validate_onetime_token(token: str, validity: str) -> models.Person:
    """Validate a one time token

    Kwargs:
        token (str): The token to validate
        validity (str): The current path

    Returns:
        person (models.Person): The validated person
    """
    if not hasattr(models, "SWOnceToken"):
        raise RuntimeError("Missing table `SWOnceToken`")

    once_token: models.SWOnceToken = (
        db.session.query(models.SWOnceToken)
        .filter(models.SWOnceToken.token == token)
        .first()
    )

    if not once_token:
        logger.warning("Unknown one time token")
        raise HTTPException(status_code=401, detail="Invalid one time token.")

    if validity != settings.api_root + once_token.validity:
        logger.warning(
            f"One time token validtiy `{once_token.validity}` and path `{validity}` do not match"
        )
        raise HTTPException(status_code=401, detail="Invalid one time token.")

    login = (
        db.session.query(models.Person.login)
        .filter(models.Person.personId == once_token.personId)
        .first()
    )
    person = get_current_person(login[0])

    db.session.delete(once_token)
    db.session.commit()

    return {
        "login": person.login,
        "personId": person.personId,
        "permissions": person._metadata["permissions"],
    }


def expire_onetime_tokens(expiry: int = 5) -> None:
    """Expire one time tokens

    Delete all tokens generated more than 10 seconds ago that are unused

    Kwargs:
        expiry (int): Seconds tokens are valid for
    """
    if not isinstance(expiry, int):
        raise RuntimeError(f"Expiry {expiry} is a none integer value")

    db.session.query(models.SWOnceToken).filter(
        models.SWOnceToken.recordTimeStamp < text(f"NOW() - INTERVAL {expiry} SECOND")
    ).delete(synchronize_session="fetch")
