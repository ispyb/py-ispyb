"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

from ispyb import app
from ispyb.auth import token_required
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema

#proposals_schema = ProposalSchema(many=True)
ns = Namespace('Sample', description='Sample related namespace', path='/sample')

@ns.route("/")
class SampleList(Resource):
    """Sample resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all sample records"""
        return 'TODO'
