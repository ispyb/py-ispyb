from fastapi import Depends, HTTPException
from pyispyb.app.base import BaseRouter
from pyispyb.app.globals import g
from pyispyb.app.extensions.auth.bearer import verify_jwt
from pyispyb.app.extensions.database.definitions import get_current_person


async def token(token: str):
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")

    g.login = decoded["username"]
    person = get_current_person()
    if not person:
        raise HTTPException(status_code=403, detail="User does not exist in database.")
    g.person = person
    g.permissions = person._metadata["permissions"]

    return token


class LegacyAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        print("LegacyAPIRouter")
        super().__init__(*args, dependencies=[Depends(token)], **kwargs)


router = LegacyAPIRouter(prefix="/legacy", tags=["Legacy"])
