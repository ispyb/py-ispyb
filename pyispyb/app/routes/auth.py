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
from sqlalchemy.exc import SQLAlchemyError
import hashlib

from pyispyb.flask_restx_patched import HTTPStatus, Resource
from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions import auth_provider
from pyispyb.app.extensions import db

from pyispyb.core import models


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Authentication",
                description="authentication namespace", path="/auth")
api_v1.add_namespace(api)


# @api.errorhandler(SQLAlchemyError)
# @api.header('ErrorType', 'SQLAlchemy Error')
# def handle_sqlalchemy_exception(error):
#     '''This is a sqlalchemy error handler'''
#     log.error(str(error))
#     return {'message': "Server error: %s" % str(error)}, HTTPStatus.BAD_REQUEST, {'ErrorType': 'SQLAlchemyError'}


# @api.errorhandler(ZeroDivisionError)
# @api.header('ErrorType', 'Zero division')
# def handle_zero_division_exception(error):
#     '''This is a zero division error'''
#     log.error(str(error))
#     return {'message': "Server error: %s" % str(error)}, HTTPStatus.BAD_REQUEST, {'ErrorType': 'ZeroDivisionError'}


# @api.errorhandler(Exception)
# @api.header('ErrorType', 'Exception')
# def handle_exception(error):
#     '''This is a base error handler'''
#     log.error(str(error))
#     print("Got the exception")
#     return {'message': "Server error: %s" % str(error)}, HTTPStatus.BAD_REQUEST, {'ErrorType': 'Exception'}

def get_param(request, name):
    res = request.headers.get(name)
    if not res:
        if request.json and request.json[name]:
            res = request.json[name]
    return res


@api.route("/login")
class Login(Resource):
    """Login resource"""

    def get(self):

        module = get_param(request, "module")
        username = get_param(request, "username")
        password = get_param(request, "password")
        token = get_param(request, "token")

        username, roles = auth_provider.get_auth(
            module, username, password, token
        )

        if not username or not roles:
            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm="Login required!"'},
            )
        else:
            token_info = auth_provider.generate_token(username, roles)
            token_ispyb = hashlib.sha1(
                token_info["token"].encode('utf-8')).hexdigest()
            bd_login = models.Login(
                token=token_ispyb,
                username=token_info["sub"],
                roles=json.dumps(token_info["roles"]),
                expirationTime=datetime.datetime.strptime(
                    token_info["exp"], "%Y-%m-%d %H:%M:%S"),
            )
            db.session.add(bd_login)
            db.session.commit()
            return token_info
