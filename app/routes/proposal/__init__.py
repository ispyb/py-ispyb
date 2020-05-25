# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.

"""
GET /proposals - Retrieves a list of proposals
GET /proposals/1 - Retrieves proposal #1
POST /proposals - Creates a new proposal
PUT /proposals/1 - Updates proposal #1
PATCH /proposals/1 - Partially updates proposal #1
DELETE /proposals/1 - Deletes proposal #1
"""


__license__ = "LGPLv3+"


import logging
from flask import request, render_template
#from flask_restx_patched import Resource
from flask_restx._http import HTTPStatus
from flask_restx import Namespace, Resource

from app.extensions import db
from app.extensions.api import api_v1 #, Namespace
from app.extensions.auth import token_required
from app.models import Proposal
from app.modules import proposal, session


log = logging.getLogger(__name__)
api = Namespace("Proposal", description="Proposal related namespace", path="/proposals")
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class Proposals(Resource):
    """Allows to get all proposals"""

    #@api.marshal_list_with(proposal.schemas.f_proposal_schema)
    #@token_required
    def get(self):
        """Returns all proposals"""
        #log.info("Return all proposals")
        page = request.args.get('page', type=int)
        if page:  
            return proposal.get_proposals_page(page)
        else:
            return proposal.get_all_proposals()

    @api.expect(proposal.schemas.f_proposal_schema)
    @api.marshal_with(proposal.schemas.f_proposal_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        log.info("Insert new proposal")

        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to create a new proposal."
            ):
            new_proposal = proposal.get_proposal_from_dict(api.payload)
            db.session.add(proposal)
        return new_proposal

@api.route("/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND,
    description="Proposal not found.",
)
#@api.resolve_object_by_model(Proposal, 'proposal')
class ProposalById(Resource):
    """Allows to get/set/delete a proposal"""

    @api.doc(description="proposal_id should be an integer ")
    # @api.marshal_with(f_proposal_schema)
    @token_required
    def get(self, proposal_id):
        """Returns a proposal by proposalId"""
        result = proposal.get_proposal_by_id(proposal_id)
        if result:
            return result, HTTPStatus.OK
        else:
            return {'message': 'Proposal with id %d not found' % proposal_id}, HTTPStatus.NOT_FOUND

    @api.expect(proposal.schemas.f_proposal_schema)
    @api.marshal_with(proposal.schemas.f_proposal_schema, code=201)
    def put(self, proposal_id):
        """Updates proposal with id proposal_id

        Args:
            proposal_id (int): corresponds to proposalId in db
        """
        log.info("Update proposal %d" % proposal_id)
        proposal.update_proposal(**api.payload)

    def delete(self, proposal_id):
        """Deletes proposal by proposal_id

        Args:
            proposal_id (int): corresponds to proposalId in db

        Returns:
            json, status_code: 
        """

        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to delete the proposal."
            ):
            proposal_item = proposal.get_proposal_item_by_id(proposal_id)
            db.session.delete(proposal_item)
        return None

@api.route("/<string:login_name>")
# @api.param("proposal_id", "Proposal id")
@api.doc(security="apikey")
class ProposalByLogin(Resource):
    """Allows to get proposal by person login name"""

    @api.doc(description="login_name should be a string")
    @api.marshal_with(proposal.schemas.f_proposal_schema)
    # @token_required
    def get(self, login_name):
        """Returns a proposal by login"""
        # app.logger.info("Returns all proposals for user with login name %s" % login_name)
        return proposal.get_proposals_by_login_name(login_name)

@api.route("/<int:proposal_id>/sessions")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(security="apikey")
class Proposal(Resource):
    """Allows to get sessions"""

    @api.doc(description="proposal_id should be an integer ")
    # @api.marshal_with(f_proposal_schema)
    @token_required
    def get(self, proposal_id):
        """Returns a proposal by proposalId"""
        return
        #return proposal.get_proposal_by_id(proposal_id)
