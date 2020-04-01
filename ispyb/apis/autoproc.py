from flask_restplus import Namespace, Resource
from ispyb import app
#from ispyb.models import Proposal
#from ispyb.schemas import ProposalSchema
from ispyb.auth import token_required

#proposals_schema = ProposalSchema(many=True)
ns = Namespace('Auto processing', description='Auto processing related namespace', path='/autoproc')

@ns.route("/")
class AutoProcList(Resource):
    """Auto processing resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all auto processing results"""
        return 'TODO'
        #app.logger.info('')
        #proposals = Proposal.query.all()
        #return proposals_schema.dump(proposals)
