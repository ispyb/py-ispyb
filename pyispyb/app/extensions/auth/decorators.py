from functools import wraps

from flask import current_app, request
from flask_restx._http import HTTPStatus

from pyispyb.app.extensions.auth import auth_provider, decode_token
from pyispyb.core.modules.proposal import loginAuthorizedForProposal
from pyispyb.core.modules.session import loginAuthorizedForSession


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

        user_info, msg = decode_token(token)
        if not user_info:
            return {"message": msg}, HTTPStatus.UNAUTHORIZED
        else:
            return func(*args, **kwargs)

    return decorated


def role_required(func):
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

        user_info = auth_provider.get_user_info_from_auth_header(
            request.headers.get("Authorization")
        )
        request.roles = user_info.get("roles", [])

        methods = current_app.config.get(
            "AUTHORIZATION_RULES").get(self.endpoint, {})
        # If no role is defined then just administrate is allowed to access the resource
        roles = methods.get(func.__name__, ["administrate"])

        if (
            "all" in roles
            or any(role in list(roles) for role in list(user_info.get("roles", [])))
        ):
            return func(self, *args, **kwargs)
        else:
            msg = "User %s (roles assigned: %s) has no appropriate role (%s) " % (
                user_info.get("sub"),
                str(user_info.get("roles")),
                str(roles),
            )
            msg += " to execute method."
            return {"message": msg}, HTTPStatus.UNAUTHORIZED

    return decorated


def check_proposal_authorization(func):

    @wraps(func)
    def decorated(self, *args, **kwargs):

        proposal_id = request.view_args["proposal_id"]
        if not proposal_id:
            proposal_id = request.view_args["proposalId"]

        if not proposal_id:
            return {"message": "No proposal_id specified"}, HTTPStatus.UNAUTHORIZED

        user_info = auth_provider.get_user_info_from_auth_header(
            request.headers.get("Authorization")
        )
        roles = user_info.get("roles", [])

        msg = ""

        if "all_proposals" in roles:
            return func(self, *args, **kwargs)
        elif "own_proposals" in roles:
            isAutorized = loginAuthorizedForProposal(
                user_info["sub"],
                proposal_id
            )
            if isAutorized:
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (roles assigned: %s) is not authorized to access proposal %s." % (
                    user_info.get("sub"),
                    str(user_info.get("roles")),
                    str(proposal_id),
                )
        else:
            msg = "User %s (roles assigned: %s) has no appropriate role (%s) to execute method." % (
                user_info.get("sub"),
                str(user_info.get("roles")),
                str(["all_proposals", "own_proposals"]),
            )

        return {"message": msg}, HTTPStatus.UNAUTHORIZED

    return decorated


def check_session_authorization(func):

    @wraps(func)
    def decorated(self, *args, **kwargs):

        session_id = request.view_args["session_id"]
        if not session_id:
            session_id = request.view_args["sessionId"]

        if not session_id:
            return {"message": "No session_id specified"}, HTTPStatus.UNAUTHORIZED

        user_info = auth_provider.get_user_info_from_auth_header(
            request.headers.get("Authorization")
        )
        roles = user_info.get("roles", [])

        msg = ""

        if "all_sessions" in roles:
            return func(self, *args, **kwargs)
        elif "own_sessions" in roles:
            isAutorized = loginAuthorizedForSession(
                user_info["sub"],
                session_id
            )
            if isAutorized:
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (roles assigned: %s) is not authorized to access session %s." % (
                    user_info.get("sub"),
                    str(user_info.get("roles")),
                    str(session_id),
                )
        else:
            msg = "User %s (roles assigned: %s) has no appropriate role (%s) to execute method." % (
                user_info.get("sub"),
                str(user_info.get("roles")),
                str(["all_sessions", "own_sessions"]),
            )

        return {"message": msg}, HTTPStatus.UNAUTHORIZED

    return decorated
