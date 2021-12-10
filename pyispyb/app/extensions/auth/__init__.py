"""
Project: py-ispyb
https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import datetime
import importlib
from functools import wraps

import jwt
from flask import current_app, request
from flask_restx._http import HTTPStatus

from pyispyb.app.utils import getSQLQuery, queryResultToDict


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users and create tokens."""

    def __init__(self):
        self.site_authentications = {}

    def init_app(self, app):
        auth_list = app.config["AUTH"]
        for auth_module in auth_list:
            for auth_name in auth_module:
                module_name = auth_module[auth_name]["AUTH_MODULE"]
                class_name = auth_module[auth_name]["AUTH_CLASS"]
                cls = getattr(importlib.import_module(module_name), class_name)
                instance = cls()
                instance.init_app(app)
                self.site_authentications[auth_name] = instance

        assert app.config["SECRET_KEY"], "SECRET_KEY must be configured!"

    def get_auth(self, module, username, password, token):
        """
        Returns roles associated to user. Basically this is the main
        authentification method where site_auth is site specific authentication
        class.

        Args:
            username (str): username
            password (str): password

        Returns:
            tuple or list: tuple or list with roles associated to the username
        """
        if not self.site_authentications[module]:
            return None
        username, roles = self.site_authentications[module].get_auth(
            username, password, token
        )
        if roles is not None and username is not None:
            return username, roles
        return None, None

    def get_user_info_from_auth_header(self, auth_header):
        """
        Returns dict with user info based on auth header.

        Args:
            auth_header ([type]): [description]

        Returns:
            dict: {"username": "", "roles": [], "is_admin": bool}
        """
        user_info = {}
        token = None

        try:
            parts = auth_header.split()
            token = parts[1]
            if current_app.config.get("MASTER_TOKEN") == token:
                user_info["sub"] = "MasterToken"
                #user_info["roles"] = current_app.config.get("ADMIN_ROLES")
                user_info["roles"] = ["manager"]
            else:
                user_info, msg = decode_token(token)
            user_info["is_admin"] = any(
                role in current_app.config.get("ADMIN_ROLES", [])
                for role in user_info["roles"]
            )

        except BaseException as ex:
            print("Unable to extract token from Authorization header (%s)" % str(ex))

        return user_info

    def generate_token(self, username, roles):
        """
        Generates token.

        Args:
            username (string): username
            roles (list): list of roles associated to the user

        Returns:
            str: token
        """
        iat = datetime.datetime.utcnow()
        exp = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=current_app.config["TOKEN_EXP_TIME"]
        )

        token = jwt.encode(
            {"sub": username, "roles": roles, "iat": iat, "exp": exp},
            current_app.config["SECRET_KEY"],
            algorithm=current_app.config["JWT_CODING_ALGORITHM"],
        )

        # TravisCI fix
        if not isinstance(token, str):
            token = token.decode("UTF-8")

        return {
            "sub": username,
            "token": token,
            "iat": iat.strftime("%Y-%m-%d %H:%M:%S"),
            "exp": exp.strftime("%Y-%m-%d %H:%M:%S"),
            "roles": roles,
        }


auth_provider = AuthProvider()


def decode_token(token):
    user_info = {}
    msg = None

    try:
        user_info = jwt.decode(
            token,
            current_app.config["SECRET_KEY"],
            algorithms=current_app.config["JWT_CODING_ALGORITHM"],
        )
    except jwt.ExpiredSignatureError:
        current_app.logger.info("Token expired. Please log in again")
        msg = "Token expired. Please log in again"
        current_app.logger.info(msg)
    except jwt.InvalidTokenError:
        msg = "Invalid token. Please log in again"
        current_app.logger.info(msg)

    return user_info, msg
