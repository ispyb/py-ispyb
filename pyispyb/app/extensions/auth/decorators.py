from functools import wraps

from flask import current_app, request
from flask_restx._http import HTTPStatus

from pyispyb.app.extensions.auth import auth_provider, decode_token
from pyispyb.core.modules.proposal import findProposalId, loginAuthorizedForProposal
from pyispyb.core.modules.session import loginAuthorizedForSession


def authentication_required(func):
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

        user_info, msg = auth_provider.get_user_info(request)
        request.user = user_info
        if not user_info:
            return {"message": msg}, HTTPStatus.UNAUTHORIZED
        else:
            return func(*args, **kwargs)

    return decorated


def permission_required(operator, roles):
    operator = operator.lower()
    if operator != "any" and operator != "all":
        raise Exception("operator must be 'any' or 'all'.")

    def decorator(func):
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

            user_info, msg = auth_provider.get_user_info(request)
            if not user_info:
                return {"message": msg}, HTTPStatus.UNAUTHORIZED

            request.roles = user_info.get("roles", [])

            if (
                (
                    operator == "any" and
                    (
                        "all" in roles
                        or any(role in list(roles) for role in list(user_info.get("roles", [])))
                    )
                )
                or
                (
                    operator == "all" and
                    (
                        all(role in list(roles)
                            for role in list(user_info.get("roles", [])))
                    )
                )

            ):
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (roles assigned: %s) has no appropriate role (%s: %s) " % (
                    user_info.get("sub"),
                    str(user_info.get("roles")),
                    operator,
                    str(roles),
                )
                msg += " to execute method."
                return {"message": msg}, HTTPStatus.UNAUTHORIZED

        return decorated
    return decorator


def proposal_authorization_required(func):

    @ wraps(func)
    def decorated(self, *args, **kwargs):

        proposal_id = request.view_args["proposal_id"]
        if not proposal_id:
            proposal_id = request.view_args["proposalId"]

        if not proposal_id:
            return {"message": "No proposal_id specified"}, HTTPStatus.UNAUTHORIZED

        proposal_id = findProposalId(proposal_id)

        user_info, msg = auth_provider.get_user_info(request)
        if not user_info:
            return {"message": msg}, HTTPStatus.UNAUTHORIZED

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


def session_authorization_required(func):

    @ wraps(func)
    def decorated(self, *args, **kwargs):

        session_id = request.view_args["session_id"]
        if not session_id:
            session_id = request.view_args["sessionId"]

        if not session_id:
            return {"message": "No session_id specified"}, HTTPStatus.UNAUTHORIZED

        user_info, msg = auth_provider.get_user_info(request)
        if not user_info:
            return {"message": msg}, HTTPStatus.UNAUTHORIZED

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
