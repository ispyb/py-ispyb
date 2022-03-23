from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pyispyb.app.extensions.database.session import get_session
from pyispyb.core import models
from pyispyb.app.globals import g
from sqlalchemy.orm import Session
import jwt

from .token import decode_token

security = HTTPBearer()


def verify_jwt(token: str):
    try:
        return decode_token(token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=403, detail="Token expired. Please log in again"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")


async def JWTBearer(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_session),
):
    if credentials:
        if not credentials.scheme == "Bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme."
            )
        decoded = verify_jwt(credentials.credentials)
        if not decoded:
            raise HTTPException(
                status_code=403, detail="Invalid token or expired token."
            )

        g.login = decoded["username"]
        person = db.query(models.Person).filter(models.Person.login == g.login).first()
        if not person:
            raise HTTPException(
                status_code=403, detail="User does not exist in database."
            )
        g.person = person

        return credentials.credentials
    else:
        raise HTTPException(status_code=403, detail="No token provided.")
