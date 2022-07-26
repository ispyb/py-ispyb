import logging
from typing import Optional

from pydantic import BaseModel
from fastapi import Request, status, HTTPException

from ..extensions.database.middleware import db
from ..extensions.database.definitions import get_current_person
from ..extensions.auth import auth_provider
from ..extensions.auth.token import generate_token
from ..base import BaseRouter


class Login(BaseModel):
    plugin: Optional[str]
    login: Optional[str]
    password: Optional[str]
    # keycloak token, not jwt (!)
    token: Optional[str]


class TokenResponse(BaseModel):
    login: str
    token: str
    permissions: list[str]


logger = logging.getLogger(__name__)
router = BaseRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    responses={401: {"description": "Could not login user"}},
)
def login(login_details: Login, request: Request) -> TokenResponse:
    """Login a user"""
    person = auth_provider.get_auth(**login_details.dict())
    if not person:
        raise HTTPException(status_code=401, detail="Could not verify")

    person_check = get_current_person(person.login)
    if not person_check:
        if request.app.db_options.create_person_on_missing:
            if not person:
                logger.warning("Could not create person from login `{login}`")
                return
            db.session.add(person)
            db.session.commit()
            person_check = person
            logger.info("Created new Person `{person.personId}` for `{login}`")
        else:
            raise HTTPException(
                status_code=401, detail="User does not exist in database."
            )

    token_info = generate_token(
        person_check.login,
        person_check.personId,
        person_check._metadata["permissions"],
    )

    return token_info
