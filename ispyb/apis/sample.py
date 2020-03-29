from flask_restplus import Namespace, Resource
from ispyb import app
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema
from ispyb.auth import token_required

#proposals_schema = ProposalSchema(many=True)
ns = Namespace('Sample', description='Sample related namespace', path='sample')

@ns.route("/list")
class SampleList(Resource):
    """Sample resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all sample records"""
        return 'TODO'
