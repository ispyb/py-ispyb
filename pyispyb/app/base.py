from fastapi import APIRouter, Depends
from .extensions.auth.bearer import jwt_bearer
from fastapi.routing import APIRoute


class BaseRouter(APIRouter):
    pass


def custom_generate_unique_id(route: APIRoute):
    res = f"{route.name}"
    return res


class AuthenticatedAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, dependencies=[Depends(jwt_bearer)], **kwargs, generate_unique_id_function=custom_generate_unique_id)
