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


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users and create tokens."""

    def __init__(self):
        self.tokens = []
        self.site_auth = None

    def init_app(self, app):
        module_name = app.config["AUTH_MODULE"]
        class_name = app.config["AUTH_CLASS"]
        cls = getattr(importlib.import_module(module_name), class_name)
        self.site_auth = cls()
        self.site_auth.init_app(app)

        assert app.config["SECRET_KEY"], "SECRET_KEY must be configured!"

        if app.config.get("MASTER_TOKEN"):
            self.tokens.append(
                {
                    "username": "admin",
                    "token": app.config.get("MASTER_TOKEN"),
                    "roles": ["admin"],
                }
            )

    def get_roles(self, username, password):
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
        return self.site_auth.get_roles(username, password)

    def get_roles_by_token(self, token):
        """
        Returns roles associated with the token.

        Args:
            token (str): jwt token

        Returns:
            tuple: tuple with roles associated to the token, user
        """
        roles = []
        if current_app.config.get("MASTER_TOKEN") == token:
            roles.append("admin")
        else:
            for user_token in self.tokens:
                if user_token["token"] == token:
                    roles = user_token["roles"]
        return roles

    def get_user_info_by_auth_header(self, auth_header):
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
        except BaseException as ex:
            print("Unable to extract token from Authorization header (%s)" % str(ex))

        for token_info in self.tokens:
            if token_info["token"] == token:
                user_info = token_info
        if user_info.get("roles"):
            user_info["is_admin"] = any(
                x in ["manager", "admin"] for x in user_info.get("roles")
            )
        else:
            user_info["is_admin"] = False

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


auth_provider = AuthProvider()


def token_required(func):
    """
    Token required decorator.

    Checks if the token is valid

    Args:
        func (method): python method

    Returns:
        func: if success
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        """
        Actual decorator function

        Returns:
            [type]: [description]
        """
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
                return func(*args, **kwargs)
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
        return func(*args, **kwargs)

    return decorated


def authorization_required(func):
    """
    Checks if user has role required to access the given resource.

    Authorization is done via AUTHORIZATION_RULES dictionary that contains
    mapping of endpoints with user groups. For example: 

    AUTHORIZATION_RULES = {
        "proposals": {
            "get": ["all"],
            "post": ["admin"]
        }
    
    define that method GET of endpoint proposals is available for all user groups
    and method POST is accessible just for admin group.
    If an endpoint is not defined in the AUTHORIZATION_RULES then it is available
    for all user groups.

    Args:
        func (function): function

    Returns:
        function: [description]
    """

    @wraps(func)
    def decorated(self, *args, **kwargs):
        """
        Actual decorator function

        Returns:
            [type]: [description]
        """

        user_info = auth_provider.get_user_info_by_auth_header(
            request.headers.get("Authorization")
        )

        methods = current_app.config.get("AUTHORIZATION_RULES").get(self.endpoint, {})
        roles = methods.get(func.__name__, [])

        print("User roles: %s" % str(user_info.get("roles")))
        print("Endpoint [%s] %s roles: %s" % (func.__name__, self.endpoint, roles))

        if not roles or "all" in roles or any(role in list(roles) for role in list(user_info.get("roles"))):
            return func(self, *args, **kwargs)
        else:
            msg = "User %s (roles assigned: %s) has no appropriate role (%s) " % (
                user_info.get("username"),
                str(user_info.get("roles")),
                str(roles),
            )
            msg += " to execute method."
            return ({"message": msg}, HTTPStatus.UNAUTHORIZED)

        return func(self, *args, **kwargs)

    return decorated
