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
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from functools import wraps

import jwt
from flask import current_app, request

from .auth_provider import AuthProvider


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if token is in header
        if "token" in request.headers:
            token = request.headers["token"]
        # Check if token is in args
        if not token:
            token = request.args.get("token")
        if not token:
            return {"message": "Token is missing."}, 401

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
            return {"message": "Token expired. Please log in again"}, 401
        except jwt.InvalidTokenError:
            print("Invalid token. Please log in again")
            return {"message": "Invalid token. Please log in again"}, 401
        return f(*args, **kwargs)

    return decorated
