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


from flask import request, make_response

from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions import auth_provider


__license__ = "LGPLv3+"


api = Namespace("Authentication", description="authentication namespace", path="/auth")
api_v1.add_namespace(api)


@api.route("/login")
class Login(Resource):
    """Login resource"""

    def get(self):
        authorization = request.authorization

        if (
            not authorization
            or not authorization.username
            or not authorization.password
        ):
            if not request.headers.get("username") or not request.headers.get(
                "password"
            ):
                return make_response(
                    "Could not verify",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Login required!"'},
                )
            else:
                username = request.headers.get("username")
                password = request.headers.get("password")
        else:
            username = authorization.username
            password = authorization.password

        roles = auth_provider.get_roles(username, password)
        if not roles:
            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm="Login required!"'},
            )
        else:
            token_info = auth_provider.generate_token(username, roles)
            return token_info