from typing import Optional

from pydantic import BaseModel
from fastapi import status, HTTPException

from ..extensions.auth import auth_provider
from ..extensions.auth.token import generate_token
from ..extensions.database.definitions import get_current_person
from ..base import BaseRouter


class Login(BaseModel):
    plugin: Optional[str]
    username: Optional[str]
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
    login = auth_provider.get_auth(**login_details.dict())

    if not login:
        raise HTTPException(status_code=401, detail="Could not verify")

    person = get_current_person(login)
    if not person:
        if False:  # request.app.db_options.create_person_on_missing:
            pass
        else:
            raise HTTPException(
                status_code=401, detail="User does not exist in database."
            )

    else:
        token_info = generate_token(
            login,
            person.personId,
            person._metadata["permissions"],
            person.familyName,
            person.givenName,
        )

        return token_info
