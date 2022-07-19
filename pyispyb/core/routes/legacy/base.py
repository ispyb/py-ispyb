from fastapi import Depends, HTTPException
from fastapi.routing import APIRoute

from pyispyb.app.base import BaseRouter
from pyispyb.app.extensions.auth.token import set_token_data
from pyispyb.app.extensions.auth.bearer import verify_jwt


async def token(token: str):
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")

    set_token_data(decoded)
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
