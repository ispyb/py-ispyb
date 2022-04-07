import datetime
import jwt

from pyispyb.config import settings


def generate_token(username, groups, permissions):
    """
    Generate token.

    Args:
        username (string): username
        groups (list): list of groups associated to the user
        permissions (list): list of permissions associated to the user

    Returns:
        str: token
    """
    iat = datetime.datetime.utcnow()
    exp = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=settings.token_exp_time
    )

    token = jwt.encode(
        {"username": username, "groups": groups,
            "permissions": permissions, "iat": iat, "exp": exp},
        settings.secret_key,
        algorithm=settings.jwt_coding_algorithm,
    )

    return {
        "username": username,
        "token": token,
        "iat": iat.strftime("%Y-%m-%d %H:%M:%S"),
        "exp": exp.strftime("%Y-%m-%d %H:%M:%S"),
        "groups": groups,
        "permissions": permissions
    }


def decode_token(token):
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
