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

from pyispyb.app.extensions.authentication import authentication_provider


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


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

        query_dict = request.args.to_dict()
        user_info = authentication_provider.get_user_info_from_auth_header(
            request.headers.get("Authorization")
        )

        methods = current_app.config.get("AUTHORIZATION_RULES").get(self.endpoint, {})
        # If no role is defined then just manager is allowed to access the resource
        roles = methods.get(func.__name__, ["manager"])

        user_allowed = False
        msg = "User %s is not to allowed to access the resource %s" % (
            user_info.get("sub"),
            str(self.endpoint)
        )

        if user_info["is_admin"]:
            user_allowed = True
        elif (
            not roles
            or "all" in roles
            or any(role in list(roles) for role in list(user_info.get("roles", [])))
        ):
            if not "proposalId" in query_dict:
                msg += "No proposalId in query arguments"
            elif query_dict["proposalId"] not in user_info["propoal_ids"]:
                msg += "Proposal with id %d not associated with the user" % query_dict["proposalId"]
            else:
                user_allowed = True

        if user_allowed:
            return func(self, *args, **kwargs)
        else:
            return {"message": msg}, HTTPStatus.UNAUTHORIZED

    return decorated
