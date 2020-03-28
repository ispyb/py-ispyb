from flask_restplus import Namespace, Resource
from ispyb import app
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema
from ispyb.auth import authorizations, token_required

#proposals_schema = ProposalSchema(many=True)
api = Namespace('dc', descriptiom='Data collection related namespace')

@api.route("/list")
class DataCollectionList(Resource):
    """Proposals resource"""

    @api.doc(security="apikey")
    @token_required
    def get(self):
        """Returns all proposal"""
        return 'TODO'
        #app.logger.info('')
        #proposals = Proposal.query.all()
        #return proposals_schema.dump(proposals)
