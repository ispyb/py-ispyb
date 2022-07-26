import datetime
import jwt
from typing import Any

from ....config import settings
from ...globals import g


def generate_token(
    login: str,
    personId: int,
    permissions: list[str],
):
    """
    Generate token.

    Args:
        login (string): login
        personid: (int): Person.personid
        permissions (list): list of permissions associated to the user

    Returns:
        str: token
    """
    iat = datetime.datetime.utcnow()
    exp = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=settings.token_exp_time
    )

    token = jwt.encode(
        {
            "login": login,
            "personId": personId,
            "permissions": permissions,
            "iat": iat,
            "exp": exp,
        },
        settings.secret_key,
        algorithm=settings.jwt_coding_algorithm,
    )

    return {
        "login": login,
        "personId": personId,
        "token": token,
        "iat": iat.strftime("%Y-%m-%d %H:%M:%S"),
        "exp": exp.strftime("%Y-%m-%d %H:%M:%S"),
        "permissions": permissions,
    }


def decode_token(token: str) -> dict[str, Any]:
    """Decode authentication token.

    Args:
        token (str): authentication token

    Returns:
        user_info: object describing user
        msg: error if present
    """
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=settings.jwt_coding_algorithm,
    )


def set_token_data(token: dict[str, Any]) -> None:
    g.login = token["login"]
    g.personId = token["personId"]
    g.permissions = token["permissions"]
