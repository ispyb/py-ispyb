from flask_restplus import Namespace, Resource
from ispyb import app
from ispyb.models import Proposal as ProposalModel
from ispyb.schemas import ProposalSchema
from ispyb.auth import authorizations, token_required

proposal_schema = ProposalSchema()
proposals_schema = ProposalSchema(many=True)
ns = Namespace('Proposals', description='Proposals related namespace', path='prop')

@ns.route("/list")
class ProposalsList(Resource):
    """Allows to get all proposals"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all proposals"""
        #app.logger.info('')
        proposals = ProposalModel.query.all()
        return proposals_schema.dump(proposals)

@ns.route("/<int:prop_id>")
@ns.param("prop_id", "Proposal id")
class Proposal(Resource):
    """Allows to get/set/delete a proposal"""

    @ns.doc(description='prop_id should be an integer ')
    #@api.marshal_with(todo)
    def get(self, prop_id):
        """Returns a proposal by proposalId"""
        proposal = ProposalModel.query.filter_by(proposalId=prop_id).first()
        return proposal_schema.dump(proposal)

    #def put(self, proposal_id):
    #    return ''
