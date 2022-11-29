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


__license__ = "LGPLv3+"

from fastapi import Depends
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.app.extensions.auth.bearer import permission_required
from pyispyb.app.globals import g
from pyispyb.core.modules.legacy import proposal
from pyispyb.core.routes.legacy.dependencies import proposal_authorisation

from .base import router as legacy_router

router = AuthenticatedAPIRouter(
    prefix="/legacy/proposals", tags=["Proposals - legacy with header token"]
)


@legacy_router.get(
    "/{token}/proposal/list",
)
@router.get(
    "",
)
def get_proposals(
    permissions=Depends(permission_required("any", ["own_proposals", "all_proposals"]))
):
    """Get all proposal that user is allowed to access."""
    if "all_proposals" in permissions:
        return proposal.get_proposals_infos_all()
    return proposal.get_proposals_infos_login(g.login)


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/info/get",
)
@router.get(
    "/{proposal_id}",
)
def get_proposal(proposal_id: str = Depends(proposal_authorisation)):
    """Get proposal information.

    Args:
        proposal_id (str): proposal id or name
    """
    proposal_id = proposal.find_proposal_id(proposal_id)
    return proposal.get_proposal_infos(proposal_id)
