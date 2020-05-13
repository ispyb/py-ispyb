"""
ISPyB flask server
"""
import logging
from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.extensions.auth import token_required
from app.modules import proposal


log = logging.getLogger(__name__)
api = Namespace("Proposal", description="Proposal related namespace", path="/prop")
api_v1.add_namespace(api)


@api.route("/list")
class ProposalList(Resource):
    """Allows to get all proposals"""

    @api.doc(security="apikey")
    @api.marshal_list_with(proposal.schemas.f_proposal_schema)
    #@token_required
    def get(self):
        """Returns all proposals"""
        log.info("Return all proposals")
        return proposal.get_all_proposals()

    @api.expect(proposal.schemas.f_proposal_schema)
    @api.marshal_with(proposal.schemas.f_proposal_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        log.info("Insert new proposal")
        proposal.add_proposal(**api.payload)

@api.route("/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
# @use_args({"name": fields.Int(required=True)}, location="headers")
class Proposal(Resource):
    """Allows to get/set/delete a proposal"""

    @api.doc(description="proposal_id should be an integer ")
    # @api.marshal_with(f_proposal_schema)
    @token_required
    def get(self, proposal_id):
        """Returns a proposal by proposalId"""
        return proposal.get_proposal_by_id(proposal_id)

    """
    #@api.doc(parser=parser)
    @api.expect(f_proposal_schema)
    def post(self, proposal_id):
        json_data = request.form['data']
        print(json_data)
        data = ma_proposal_schema.load(json_data)

    """


@api.route("/login_name/<string:login_name>")
# @api.param("proposal_id", "Proposal id")
class ProposalByLogin(Resource):
    """Allows to get proposal by person login name"""

    @api.doc(description="login_name should be a string")
    @api.marshal_with(proposal.schemas.f_proposal_schema)
    # @token_required
    def get(self, login_name):
        """Returns a proposal by login"""
        # app.logger.info("Returns all proposals for user with login name %s" % login_name)
        return proposal.get_proposals_by_login_name(login_name)

