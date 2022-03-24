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

from pyispyb.core.modules.legacy.proposal import find_proposal_id
from pyispyb.core.modules import session
from pyispyb.app.globals import g

__license__ = "LGPLv3+"


from .base import router


@router.get(
    "/{token}/session/list",
)
def get_sessions():
    """Get all sessions that user is allowed to access."""
    if "all_sessions" in g.permissions:
        return session.get_session_infos_all()
    return session.get_session_infos_login(g.login)


@router.get(
    "/{token}/proposal/session/date/{start_date}/{end_date}/list",
)
def get_sessions_by_dates(start_date: str, end_date: str):
    """Get all sessions between two dates that user is allowed to access.

    Args:
        start_date (str): start date
        end_date (str): end date
    """
    if "all_sessions" in g.permissions:
        return session.get_session_infos_all_dates(start_date, end_date)
    return session.get_session_infos_login_dates(
        g.login, start_date, end_date
    )


@router.get(
    "/{token}/proposal/{proposal_id}/session/list",
)
def get_sessions_for_proposal(self, proposal_id: int, **kwargs):
    """Get all sessions for proposal that user is allowed to access.

    Args:
        proposal_id (str): proposal id or name
    """
    proposal_id = find_proposal_id(proposal_id)
    if "all_sessions" in g.permissions:
        return session.get_session_infos_all_proposal(proposal_id)
    return session.get_session_infos_login_proposal(
        g.login, proposal_id
    )
