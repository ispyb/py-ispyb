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


__license__ = "LGPLv3+"


from functools import wraps

import jwt
from flask import current_app, request
from flask_restx._http import HTTPStatus

from .auth_provider import AuthProvider


auth_provider = AuthProvider()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        auth = request.headers.get("Authorization", None)
        if not auth:
            return (
                {"message": "Authorization header is expected"},
                HTTPStatus.UNAUTHORIZED,
            )

        parts = auth.split()

        if parts[0].lower() != "bearer":
            return (
                {"message": "Authorization header must start with Bearer"},
                HTTPStatus.UNAUTHORIZED,
            )
        elif len(parts) == 1:
            return {"message": "Token not found"}, HTTPStatus.UNAUTHORIZED
        elif len(parts) > 2:
            return (
                {"message": "Authorization header must be Bearer token"},
                HTTPStatus.UNAUTHORIZED,
            )

        token = parts[1]

        if current_app.config.get("MASTER_TOKEN"):
            if current_app.config["MASTER_TOKEN"] == token:
                current_app.logger.info("Master token validated")
                return f(*args, **kwargs)
        try:
            jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=current_app.config["JWT_CODING_ALGORITHM"],
            )
        except jwt.ExpiredSignatureError:
            current_app.logger.info("Token expired. Please log in again")
            print("Token expired. Please log in again")
            return (
                {"message": "Token expired. Please log in again"},
                HTTPStatus.UNAUTHORIZED,
            )
        except jwt.InvalidTokenError:
            print("Invalid token. Please log in again")
            return (
                {"message": "Invalid token. Please log in again"},
                HTTPStatus.UNAUTHORIZED,
            )
        return f(*args, **kwargs)

    return decorated

def write_permission_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            auth = request.headers.get("Authorization", None)
            parts = auth.split()
            token = parts[1]
            roles = auth_provider.get_roles_by_token(token)
            return f(*args, **kwargs)
        except:
            return (
                {"message": "User has no write permission"},
                HTTPStatus.UNAUTHORIZED,
            )

    return decorated
