from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
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

        g.username = decoded["username"]
        g.permissions = decoded["permissions"]
        g.groups = decoded["groups"]

        return credentials.credentials
    else:
        raise HTTPException(status_code=401, detail="No token provided.")
