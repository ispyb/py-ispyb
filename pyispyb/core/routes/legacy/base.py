from fastapi import Depends, HTTPException
from pyispyb.app.base import BaseRouter
from pyispyb.app.globals import g
from pyispyb.app.extensions.auth.bearer import verify_jwt


async def token(token: str):
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(
            status_code=401, detail="Invalid token or expired token."
        )

    g.username = decoded["username"]
    g.permissions = decoded["permissions"]
    g.groups = decoded["groups"]

    return token


class LegacyAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, dependencies=[Depends(token)], **kwargs)


router = LegacyAPIRouter(prefix="/legacy", tags=["Legacy"])
