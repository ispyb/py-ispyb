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

import datetime
import json
import hashlib
from typing import Optional
from pydantic import BaseModel
from fastapi import status, HTTPException

from pyispyb.app.extensions.auth import auth_provider
from pyispyb.app.extensions.database.middleware import db

from pyispyb.core import models
from ..base import BaseRouter


__license__ = "LGPLv3+"


class Login(BaseModel):
    plugin: Optional[str]
    username: str
    password: str
    # keycloak token, not jwt (!)
    token: Optional[str]


class TokenResponse(BaseModel):
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
        login.username, login.password, login.token
    )

    if not username:
        raise HTTPException(status_code=401, detail="Could not verify")

    else:
        token_info = auth_provider.generate_token(username, groups, permissions)

        if hasattr(models, "Login"):
            token_ispyb = hashlib.sha1(token_info["token"].encode("utf-8")).hexdigest()

            bd_login = models.Login(
                token=token_ispyb,
                username=token_info["username"],
                roles=json.dumps(token_info["groups"]),
                expirationTime=datetime.datetime.strptime(
                    token_info["exp"], "%Y-%m-%d %H:%M:%S"
                ),
            )
            db.session.add(bd_login)
            db.session.commit()

        return token_info
