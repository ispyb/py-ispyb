from fastapi import Depends, HTTPException
from pyispyb.app.base import BaseRouter
from pyispyb.app.globals import g
from pyispyb.app.extensions.auth.bearer import verify_jwt
from fastapi.routing import APIRoute


async def token(token: str):
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

    g.username = decoded["username"]
    g.permissions = decoded["permissions"]
    g.groups = decoded["groups"]

    return token


def custom_generate_unique_id(route: APIRoute):
    res = f"{route.name}-legacy_token"
    return res


class LegacyAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            dependencies=[Depends(token)],
            **kwargs,
            generate_unique_id_function=custom_generate_unique_id,
        )


router = LegacyAPIRouter(
    prefix="/legacy", tags=["Legacy with token in path ⚠️ only for compatibility ⚠️"]
)
