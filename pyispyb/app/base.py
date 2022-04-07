from fastapi import APIRouter, Depends
from .extensions.auth.bearer import JWTBearer


class BaseRouter(APIRouter):
    pass


class AuthenticatedAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, dependencies=[Depends(JWTBearer)], **kwargs)
