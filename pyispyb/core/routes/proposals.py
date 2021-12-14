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

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth.decorators import check_proposal_authorization, token_required, role_required
from pyispyb.core.schemas import proposal as proposal_schemas
from pyispyb.core.modules import contacts, proposal


api = Namespace(
    "Proposals", description="Proposal related namespace", path="/proposals"
)
api_v1.add_namespace(api)


@api.route("", endpoint="proposals")
@api.doc(security="apikey")
class Proposals(Resource):
    """Allows to get all proposals"""

    @token_required
    @role_required
    def get(self):
        """Returns proposals based on query parameters"""
        api.logger.info("Get all proposals")
        user_info = contacts.get_person_info(request)
        query_dict = request.args.to_dict()
        if not "all_proposals" in request.roles:
            proposal_ids = proposal.get_proposal_ids_by_person_id(
                user_info["personId"]
            )
            query_dict["proposalId"] = proposal_ids
        return proposal.get_proposals_by_query(query_dict)

    @token_required
    @role_required
    @api.expect(proposal_schemas.f_schema)
    @api.marshal_with(proposal_schemas.f_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        api.logger.info("Inserts a new proposal")
        return proposal.add_proposal(api.payload)


@api.route("/<int:proposal_id>", endpoint="proposal_by_id")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.FOUND, description="Proposal found.", model=proposal_schemas.f_schema)
@api.response(code=HTTPStatus.NOT_FOUND, description="Proposal not found.")
class ProposalById(Resource):
    """Allows to get/set/delete a proposal"""

    @token_required
    @role_required
    @check_proposal_authorization
    @api.doc(description="proposal_id should be an integer ")
    @api.marshal_with(proposal_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self, proposal_id):
        """Returns a proposal by proposalId"""
        return proposal.get_proposal_by_id(proposal_id)

    @token_required
    @role_required
    @check_proposal_authorization
    @api.expect(proposal_schemas.f_schema)
    @api.marshal_with(proposal_schemas.f_schema, code=HTTPStatus.CREATED)
    def put(self, proposal_id):
        """Fully updates proposal with id proposal_id"""
        current_app.logger.info("Update proposal %d" % proposal_id)
        return proposal.update_proposal(proposal_id, api.payload)

    @token_required
    @role_required
    @check_proposal_authorization
    @api.expect(proposal_schemas.f_schema)
    @api.marshal_with(proposal_schemas.f_schema, code=HTTPStatus.CREATED)
    def patch(self, proposal_id):
        """Partially updates proposal with id proposal_id"""
        return proposal.patch_proposal(proposal_id, api.payload)

    @token_required
    @role_required
    @check_proposal_authorization
    def delete(self, proposal_id):
        """Deletes a proposal by proposal_id"""
        return proposal.delete_proposal(proposal_id)


@api.route("/<int:proposal_id>/info", endpoint="proposal_info_by_id")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.FOUND, description="Proposal info found.")
@api.response(code=HTTPStatus.NOT_FOUND, description="Proposal info not found.")
class ProposalInfoById(Resource):
    """Returns full information of a proposal"""

    @token_required
    @role_required
    @check_proposal_authorization
    @api.doc(description="proposal_id should be an integer ")
    def get(self, proposal_id):
        """Returns a full description of a proposal by proposalId"""
        return proposal.get_proposal_info_by_id(proposal_id)
