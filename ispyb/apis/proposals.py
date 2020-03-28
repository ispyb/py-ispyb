from flask_restplus import Namespace, Resource
from ispyb import app
from ispyb.models import Proposal
from ispyb.schemas import ProposalSchema
from ispyb.auth import authorizations, token_required

proposals_schema = ProposalSchema(many=True)
api = Namespace('prop', descriptiom='Proposals related namespace')

@api.route("/list")
class ProposalsList(Resource):
    """Proposals resource"""

    @api.doc(security="apikey")
    @token_required
    def get(self):
        """Returns all proposals"""
        #app.logger.info('')
        proposals = Proposal.query.all()
        return proposals_schema.dump(proposals)
