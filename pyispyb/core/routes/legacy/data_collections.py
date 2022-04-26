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
from pyispyb.core.modules.legacy import data_collections
from pyispyb.core.routes.legacy.dependencies import session_authorisation

from .base import router as legacy_router

router = AuthenticatedAPIRouter(
    prefix="/data_collections", tags=["Data collections - legacy with header token"]
)


__license__ = "LGPLv3+"


@legacy_router.get(
    "/{token}/proposal/session/{session_id}/list",
)
@router.get("/groups/session/{session_id}")
def get(session_id: int = Depends(session_authorisation)):
    """Get data collection groups for session.

    Args:
        session_id (str): session id
    """
    return data_collections.get_data_collections_groups(session_id)
