from functools import wraps

from flask import request

from pyispyb.app.extensions.auth import auth_provider
from pyispyb.core.modules.legacy.proposal import find_proposal_id, login_authorized_for_proposal
from pyispyb.core.modules.legacy.session import login_authorized_for_session


def permission_required(operator, permissions):
    """Make the route only accesible to users with the specified permissions.

    Args:
        operator (str): any or all
        permissions (str[]): permissions required
    """
    operator = operator.lower()
    if operator != "any" and operator != "all":
        raise Exception("operator must be 'any' or 'all'.")

    def decorator(func):
        @wraps(func)
        def decorated(self, *args, **kwargs):
            user_info, msg = auth_provider.get_user_info(request)
            if not user_info:
                return {"message": msg}, HTTPStatus.UNAUTHORIZED

            request.permissions = user_info.get("permissions", [])

            if (
                (
                    operator == "any" and (
                        "all" in permissions or any(
                            permission in list(permissions) for permission in list(
                    user_info.get(
                        "permissions",
                        []))))) or (
                            operator == "all" and (
                                all(
                                    permission in list(permissions) for permission in list(
                                        user_info.get(
                                            "permissions",
                                            [])))))):
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
