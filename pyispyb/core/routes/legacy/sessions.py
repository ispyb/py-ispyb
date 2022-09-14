"""
Project: py-ispyb.

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

from fastapi import Depends
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.app.extensions.auth.bearer import permission_required
from pyispyb.core.modules.legacy.proposal import find_proposal_id
from pyispyb.core.modules.legacy import session
from pyispyb.app.globals import g

__license__ = "LGPLv3+"


from .base import router as legacy_router

router = AuthenticatedAPIRouter(
    prefix="/legacy/sessions", tags=["Sessions - legacy with header token"]
)


@legacy_router.get(
    "/{token}/session/list",
)
@router.get(
    "",
)
def get_sessions(
    permissions=Depends(permission_required("any", ["own_sessions", "all_sessions"]))
):
    """Get all sessions that user is allowed to access."""
    if "all_sessions" in permissions:
        return session.get_session_infos_all()
    return session.get_session_infos_login(g.login)


@legacy_router.get(
    "/{token}/proposal/session/date/{start_date}/{end_date}/list",
)
@router.get(
    "/date/{start_date}/{end_date}",
)
def get_sessions_by_dates(
    start_date: str,
    end_date: str,
    permissions=Depends(permission_required("any", ["own_sessions", "all_sessions"])),
):
    """Get all sessions between two dates that user is allowed to access.

    Args:
        start_date (str): start date
        end_date (str): end date
    """
    if "all_sessions" in permissions:
        return session.get_session_infos_all_dates(start_date, end_date)
    return session.get_session_infos_login_dates(g.login, start_date, end_date)


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/session/list",
)
@router.get(
    "/proposal/{proposal_id}",
)
def get_sessions_for_proposal(
    proposal_id: str,
    permissions=Depends(permission_required("any", ["own_sessions", "all_sessions"])),
):
    """Get all sessions for proposal that user is allowed to access.

    Args:
        proposal_id (str): proposal id or name
    """
    proposal_id = find_proposal_id(proposal_id)
    if "all_sessions" in permissions:
        return session.get_session_infos_all_proposal(proposal_id)
    return session.get_session_infos_login_proposal(g.login, proposal_id)
