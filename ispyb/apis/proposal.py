from flask_restplus import Namespace, Resource
from ispyb import app
from ispyb.models import Proposal as ProposalModel
from ispyb.schemas import ProposalSchema, proposal_schema
from ispyb.auth import token_required

ma_proposal_schema = ProposalSchema()
ma_proposals_schema = ProposalSchema(many=True)
ns = Namespace('Proposal', description='Proposal related namespace', path='prop')

@ns.route("/list")
class ProposalList(Resource):
    """Allows to get all proposals"""

    @ns.doc(security="apikey")
    @token_required
    def get(self):
        """Returns all proposals"""
        #app.logger.info('')
        proposals = ProposalModel.query.all()
        return ma_proposals_schema.dump(proposals)
        #return list(ProposalModel.query.all())


@ns.route("/<int:prop_id>")
@ns.param("prop_id", "Proposal id")
class Proposal(Resource):
    """Allows to get/set/delete a proposal"""

    @ns.doc(description='prop_id should be an integer ')
    @ns.marshal_with(proposal_schema)
    @token_required
    def get(self, prop_id):
        """Returns a proposal by proposalId"""
        proposal= ProposalModel.query.filter_by(proposalId=prop_id).first()
        return ma_proposal_schema.dump(proposal)
        #return ProposalModel.query.filter_by(proposalId=prop_id).first()

    #def put(self, proposal_id):
    #    return ''
