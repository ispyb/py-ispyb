from fastapi import APIRouter, Depends
from .extensions.auth.bearer import JWTBearer


class BaseRouter(APIRouter):
    pass


class AuthenticatedAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        print("AuthenticatedAPIRouter")
        # super().__init__(*args, dependencies=[Depends(JWTBearer)], **kwargs)
        super().__init__(*args, **kwargs)
