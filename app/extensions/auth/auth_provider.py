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


import datetime
import importlib

import jwt
from flask import current_app


class AuthProvider:
    """Allows to authentificate users and create tokens"""

    def __init__(self):
        self.tokens = []
        self.site_auth = None

    def init_app(self, app):
        module_name = app.config["AUTH_MODULE"]
        class_name = app.config["AUTH_CLASS"]
        cls = getattr(importlib.import_module(module_name), class_name)
        self.site_auth = cls()

        assert app.config["SECRET_KEY"], "SECRET_KEY must be configured!"

    def get_roles(self, username, password):
        """Returns roles associated to user.
        Basically this is the main authentification method where site_auth
        is site specific authentication class.

        Args:
            username (str): username
            password (str): password

        Returns:
            tuple or list: tuple or list with roles associated to the username
        """
        return self.site_auth.get_roles(username, password)

    def get_roles_by_token(self, token):
        """Returns roles associated with the token

        Args:
            token (str): jwt token

        Returns:
            tuple: tuple with roles associated to the token, user
        """
        if current_app.config.get("MASTER_TOKEN") == token:
            return "admin"
        else:
            print(self.tokens)
            for user_token in self.tokens:
                print(user_token)
                if user_token["token"] == token:
                    return user_token["roles"]

    def generate_token(self, username, roles):
        """Generates token

        Args:
            username (string): username
            roles (list): list of roles associated to the user

        Returns:
            str: token
        """
        if username in self.tokens:
            # Check if the previously generated token is still valid
            try:
                jwt.decode(
                    self.tokens[username]["token"],
                    current_app.config["SECRET_KEY"],
                    algorithms=current_app.config["JWT_CODING_ALGORITHM"],
                )
                return self.tokens[username]["token"]
            except jwt.ExpiredSignatureError:
                pass

        token = jwt.encode(
            {
                "sub": username,
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(minutes=current_app.config["TOKEN_EXP_TIME"]),
            },
            current_app.config["SECRET_KEY"],
            algorithm=current_app.config["JWT_CODING_ALGORITHM"],
        )
        dec_token = token.decode("UTF-8")

        self.tokens.append({"username": username, "token": dec_token, "roles": roles})

        return dec_token
