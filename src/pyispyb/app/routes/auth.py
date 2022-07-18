# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.

from typing import Optional
from pydantic import BaseModel
from fastapi import status, HTTPException

from pyispyb.app.extensions.auth import auth_provider
from pyispyb.app.extensions.auth.token import generate_token

from ..base import BaseRouter


__license__ = "LGPLv3+"


class Login(BaseModel):
    plugin: Optional[str]
    username: Optional[str]
    password: Optional[str]
    # keycloak token, not jwt (!)
    token: Optional[str]


class TokenResponse(BaseModel):
    username: str
    token: str
    permissions: list[str]
    groups: list[str]


router = BaseRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    responses={401: {"description": "Could not login user"}},
)
def login(login: Login) -> TokenResponse:
    """Login a user"""
    username, groups, permissions = auth_provider.get_auth(
        login.plugin, login.username, login.password, login.token
    )

    if not username:
        raise HTTPException(status_code=401, detail="Could not verify")

    else:
        token_info = generate_token(username, groups, permissions)

        return token_info
