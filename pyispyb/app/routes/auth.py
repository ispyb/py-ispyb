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
import logging
from flask import request, make_response
import hashlib

from flask_restx import Resource
from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions import auth_provider
from pyispyb.app.extensions import db

from pyispyb.core import models


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Authentication",
                description="authentication namespace", path="/auth")
api_v1.add_namespace(api)


def get_param(request, name):
    """Get param from request - look in headers, json, args, and form.

    Args:
        request (HTTP request): request
        name (string): name of the parameter to be found

    Returns:
        str: parameter value
    """
    res = request.headers.get(name)
    if not res:
        if request.json and name in request.json:
            res = request.json[name]
    if not res:
        if request.args and request.args.get(name, default=False):
            res = request.args.get(name, default=None)
    if not res:
        if request.form and request.form.get(name, default=False):
            res = request.form.get(name, default=None)
    return res


@api.route("/login")
@legacy_api.route("/authenticate")
class Login(Resource):

    def post(self):
        """Get authentication token for user.

        Returns:
            dict: token_info
        """
        plugin = get_param(request, "plugin")
        username = get_param(request, "username")
        if username is None:
            username = get_param(request, "login")
        password = get_param(request, "password")
        token = get_param(request, "token")

        username, groups, permissions = auth_provider.get_auth(
            plugin, username, password, token
        )

        if not username:
            return make_response(
                "Could not verify",
                401,
            )
        else:
            token_info = auth_provider.generate_token(
                username, groups, permissions)
            token_ispyb = hashlib.sha1(
                token_info["token"].encode('utf-8')).hexdigest()
            bd_login = models.Login(
                token=token_ispyb,
                username=token_info["username"],
                roles=json.dumps(token_info["groups"]),
                expirationTime=datetime.datetime.strptime(
                    token_info["exp"], "%Y-%m-%d %H:%M:%S"),
            )
            db.session.add(bd_login)
            db.session.commit()
            return token_info
