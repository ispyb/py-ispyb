from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pyispyb.app.extensions.database.definitions import get_current_person
from pyispyb.app.globals import g
import jwt

from .token import decode_token

security = HTTPBearer()


def verify_jwt(token: str):
    try:
        return decode_token(token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401, detail="Token expired. Please log in again"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def JWTBearer(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if credentials:
        if not credentials.scheme == "Bearer":
            raise HTTPException(
                status_code=401, detail="Invalid authentication scheme."
            )
        decoded = verify_jwt(credentials.credentials)
        if not decoded:
            raise HTTPException(
                status_code=401, detail="Invalid token or expired token."
            )

        g.login = decoded["username"]
        person = get_current_person()
        if not person:
            raise HTTPException(
                status_code=401, detail="User does not exist in database."
            )
        g.person = person
        g.permissions = person._metadata["permissions"]

        return credentials.credentials
    else:
        raise HTTPException(status_code=401, detail="No token provided.")
