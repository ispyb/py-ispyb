from functools import wraps

from flask import request
from flask_restx._http import HTTPStatus

from pyispyb.app.extensions.auth import auth_provider
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


def permission_required(operator, permissions):
    operator = operator.lower()
    if operator != "any" and operator != "all":
        raise Exception("operator must be 'any' or 'all'.")

    def decorator(func):
        """
        Checks if user has permissions required to access the given resource.
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

            request.permissions = user_info.get("permissions", [])

            if (
                (
                    operator == "any" and
                    (
                        "all" in permissions
                        or any(permission in list(permissions) for permission in list(user_info.get("permissions", [])))
                    )
                )
                or
                (
                    operator == "all" and
                    (
                        all(permission in list(permissions)
                            for permission in list(user_info.get("permissions", [])))
                    )
                )

            ):
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (permissions assigned: %s) has no appropriate permission (%s: %s) " % (
                    user_info.get("username"),
                    str(user_info.get("permissions")),
                    operator,
                    str(permissions),
                )
                msg += " to execute method."
                return {"message": msg}, HTTPStatus.UNAUTHORIZED

        return decorated
    return decorator


def proposal_authorization_required(func):

    @wraps(func)
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

        permissions = user_info.get("permissions", [])

        msg = ""

        if "all_proposals" in permissions:
            return func(self, *args, **kwargs)
        elif "own_proposals" in permissions:
            isAutorized = loginAuthorizedForProposal(
                user_info["username"],
                proposal_id
            )
            if isAutorized:
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (permissions assigned: %s) is not authorized to access proposal %s." % (
                    user_info.get("username"),
                    str(user_info.get("permissions")),
                    str(proposal_id),
                )
        else:
            msg = "User %s (permissions assigned: %s) has no appropriate permissions (%s) to execute method." % (
                user_info.get("username"),
                str(user_info.get("permissions")),
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

        permissions = user_info.get("permissions", [])

        msg = ""

        if "all_sessions" in permissions:
            return func(self, *args, **kwargs)
        elif "own_sessions" in permissions:
            isAutorized = loginAuthorizedForSession(
                user_info["username"],
                session_id
            )
            if isAutorized:
                return func(self, *args, **kwargs)
            else:
                msg = "User %s (permissions assigned: %s) is not authorized to access session %s." % (
                    user_info.get("username"),
                    str(user_info.get("permissions")),
                    str(session_id),
                )
        else:
            msg = "User %s (permissions assigned: %s) has no appropriate permissions (%s) to execute method." % (
                user_info.get("username"),
                str(user_info.get("permissions")),
                str(["all_sessions", "own_sessions"]),
            )

        return {"message": msg}, HTTPStatus.UNAUTHORIZED

    return decorated
