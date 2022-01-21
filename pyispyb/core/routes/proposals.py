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

Proposal namespace with enpoint allowing to access proposals.

Example routes:

[GET]   /ispyb/api/v1/proposals     - Retrieves a list of proposals
[GET]   /ispyb/api/v1/proposals?proposalType=MX - Retrieves a list of MX proposals
[POST]  /ispyb/api/v1/proposals    - Creates a new proposal

[GET]   /ispyb/api/v1/proposals/1  - Retrieves proposal #1
[PUT]   /ispyb/api/v1/proposals/1  - Updates proposal #1
[PATCH] /ispyb/api/v1/proposals/1  - Partially updates proposal #1
[DELETE]/ispyb/api/v1/proposals/1  - Deletes proposal #1
"""


__license__ = "LGPLv3+"

from flask import request, current_app, abort
from flask_restx._http import HTTPStatus

from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, authentication_required, permission_required
from pyispyb.core.schemas import proposal as proposal_schemas
from pyispyb.core.modules import proposal


api = Namespace(
    "Proposals", description="Proposal related namespace", path="/proposals"
)
api_v1.add_namespace(api)


@api.route("/infos", endpoint="proposals_infos")
@legacy_api.route("/<token>/proposal/list")
@api.doc(security="apikey")
class ProposalsInfosLogin(Resource):
    """Allows to get proposals associated to login"""

    @authentication_required
    @permission_required("any", "own_proposals")
    def get(self, **kwargs):
        return proposal.get_proposals_infos_login(request.user['sub'])
