# ISPyB flask server
# https://github.com/IvarsKarpics/ispyb_backend_prototype

from flask_restplus import Namespace, Resource
from ispyb import app
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema
from ispyb.auth import token_required

#proposals_schema = ProposalSchema(many=True)
ns = Namespace('Crystal', description='Crystal related namespace', path='/crystal')

@ns.route("/")
class CrystalList(Resource):
    """Crystal list resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all crystal records"""
        return 'TODO'
