from flask_restplus import Namespace, Resource
from ispyb import app
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema
from ispyb.auth import authorizations, token_required

#proposals_schema = ProposalSchema(many=True)
ns = Namespace('Data collections', description='Data collection related namespace', path='dc')

@ns.route("/list")
class DataCollectionList(Resource):
    """Data collection resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all data collections"""
        return 'TODO'
        #app.logger.info('')
        #proposals = Proposal.query.all()
        #return proposals_schema.dump(proposals)
