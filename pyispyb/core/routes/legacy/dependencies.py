from fastapi import HTTPException
from pyispyb.core.modules.legacy.proposal import (
    find_proposal_id,
    login_authorized_for_proposal,
)
from pyispyb.core.modules.legacy.session import login_authorized_for_session
from pyispyb.app.globals import g


def proposal_authorisation(proposal_id: str):
    proposal_id = find_proposal_id(proposal_id)

    permissions = g.permissions
    login = g.login

    msg = ""

    if "all_proposals" in permissions:
        return proposal_id
    elif "own_proposals" in permissions:
        is_autorized = login_authorized_for_proposal(login, proposal_id)
        if is_autorized:
            return proposal_id
        else:
            msg = (
                "User %s (permissions assigned: %s) is not authorized to access proposal %s."
                % (
                    login,
                    str(permissions),
                    str(proposal_id),
                )
            )
    else:
        msg = (
            "User %s (permissions assigned: %s) has no appropriate permissions (%s) to execute method."
            % (
                login,
                str(permissions),
                str(["all_proposals", "own_proposals"]),
            )
        )

    raise HTTPException(status_code=403, detail=msg)


def session_authorisation(session_id: str):

    permissions = g.permissions
    login = g.login

    msg = ""

    if "all_sessions" in permissions:
        return session_id
    elif "own_sessions" in permissions:
        is_autorized = login_authorized_for_session(login, session_id)
        if is_autorized:
            return session_id
        else:
            msg = (
                "User %s (permissions assigned: %s) is not authorized to access session %s."
                % (
                    login,
                    str(permissions),
                    str(session_id),
                )
            )
    else:
        msg = (
            "User %s (permissions assigned: %s) has no appropriate permissions (%s) to execute method."
            % (
                login,
                str(permissions),
                str(["all_sessions", "own_sessions"]),
            )
        )

    raise HTTPException(status_code=403, detail=msg)
