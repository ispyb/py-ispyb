from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.modules import session

api = Namespace("Session", description="Session related namespace", path="/session")
api_v1.add_namespace(api)

@api.route("/list")
class SessionList(Resource):
    @api.doc(security="apikey")
    def get(self):
        return session.get_all_sessions()


@api.route("/proposal/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(description="proposal_id should be an integer ")
# @token_required
class ProposalSessionList(Resource):
    def get(self, proposal_id):
        """Returns all proposal shippings"""
        return session.get_proposal_sessions(proposal_id)
