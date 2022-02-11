
# Project: py-ispyb
# https://github.com/ispyb/py-ispyb

# This file is part of py-ispyb software.

# py-ispyb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# py-ispyb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


import logging
import datetime
import importlib

import jwt
from flask import current_app


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users and create tokens."""

    def __init__(self):
        self.site_authentications = {}

    def init_app(self, app):
        """Init extension."""
        auth_list = app.config["AUTH"]
        for auth_plugin in auth_list:
            for auth_name in auth_plugin:
                enabled = auth_plugin[auth_name]["ENABLED"]
                if enabled:
                    module_name = auth_plugin[auth_name]["AUTH_MODULE"]
                    class_name = auth_plugin[auth_name]["AUTH_CLASS"]
                    config = {}
                    if "CONFIG" in auth_plugin[auth_name]:
                        config = auth_plugin[auth_name]["CONFIG"]
                    cls = getattr(importlib.import_module(
                        module_name), class_name)
                    instance = cls()
                    instance.configure(config)
                    self.site_authentications[auth_name] = instance

        assert app.config["SECRET_KEY"], "SECRET_KEY must be configured!"

    def get_auth(self, plugin, username, password, token):
        """
        Return username, groups, permissions associated to user.

        Basically this is the main authentification method where site_auth is site specific authentication class.

        Args:
            plugin (str): plugin to be used
            username (str): auth username
            password (str): auth password
            token (str): auth token

        Returns:
            username, groups, permissions
        """
        if plugin not in self.site_authentications:
            return None, None, None
        username, groups, permissions = self.site_authentications[plugin].get_auth(
            username, password, token)
        if username is not None and groups is not None and permissions is not None:
            return username, groups, permissions
        return None, None, None

    def get_user_info(self, request):
        """Get user infos from request.

        Args:
            request (HTTP request): request

        Returns:
            user_info: object describing user
            msg: error if present
        """
        token = None

        auth = request.headers.get("Authorization", None)
        if auth is not None:
            # AUTH HEADER -> TOKEN IS IN HEADER
            parts = auth.split()
            if parts[0].lower() != "bearer":
                None, "Authorization header must start with Bearer"
            elif len(parts) == 1:
                return None, "Token not found"
            elif len(parts) > 2:
                return None, "Authorization header must be Bearer token"
            token = parts[1]
        else:
            # NO AUTH HEADER -> TOKEN IS IN PARAMS (LEGACY ROUTES)
            token = request.view_args["token"]

        if not token:
            return None, "Authorization header is expected"

        user_info, msg = decode_token(token)
        return user_info, msg

    def generate_token(self, username, groups, permissions):
        """
        Generate token.

        Args:
            username (string): username
            groups (list): list of groups associated to the user
            permissions (list): list of permissions associated to the user

        Returns:
            str: token
        """
        iat = datetime.datetime.utcnow()
        exp = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=current_app.config["TOKEN_EXP_TIME"]
        )

        token = jwt.encode(
            {"username": username, "groups": groups,
                "permissions": permissions, "iat": iat, "exp": exp},
            current_app.config["SECRET_KEY"],
            algorithm=current_app.config["JWT_CODING_ALGORITHM"],
        )

        # TravisCI fix
        if not isinstance(token, str):
            token = token.decode("UTF-8")

        return {
            "username": username,
            "token": token,
            "iat": iat.strftime("%Y-%m-%d %H:%M:%S"),
            "exp": exp.strftime("%Y-%m-%d %H:%M:%S"),
            "groups": groups,
            "permissions": permissions
        }


auth_provider = AuthProvider()


def decode_token(token):
    """Decode authentication token.

    Args:
        token (str): authentication token

    Returns:
        user_info: object describing user
        msg: error if present
    """
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
