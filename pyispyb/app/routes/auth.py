from typing import Optional

from pydantic import BaseModel
from fastapi import status, HTTPException

from ..extensions.auth import auth_provider
from ..extensions.auth.token import generate_token
from ..base import BaseRouter


class Login(BaseModel):
    plugin: Optional[str]
    login: Optional[str]
    password: Optional[str]
    # keycloak token, not jwt (!)
    token: Optional[str]


class TokenResponse(BaseModel):
    login: str
    token: str
    permissions: list[str]


router = BaseRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    responses={401: {"description": "Could not login user"}},
)
def login(login_details: Login) -> TokenResponse:
    """Login a user"""
    person = auth_provider.get_auth(**login_details.dict())
    if not person:
        raise HTTPException(status_code=401, detail="Could not verify")

    else:
        token_info = generate_token(
            person.login,
            person.personId,
            person._metadata["permissions"],
        )

        return token_info
