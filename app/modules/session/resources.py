from flask_restx import Namespace, Resource
from app.models import BLSession as SessionModel
from app.modules.session.schemas import f_session_schema, ma_session_schema

api = Namespace("Session", description="Session related namespace", path="/session")


def get_all_sessions():
    session_list = SessionModel.query.all()
    return ma_session_schema.dump(session_list, many=True)


def get_proposal_sessions(proposal_id):
    session_list = SessionModel.query.filter_by(proposalId=proposal_id)
    return ma_session_schema.dump(session_list, many=True)

@api.route("/list")
class SessionList(Resource):

    @api.doc(security="apikey")
    def get(self):
        return get_all_sessions()


@api.route("/proposal/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(description="proposal_id should be an integer ")
#@token_required
class ProposalSessionList(Resource):

    def get(self, proposal_id):
        """Returns all proposal shippings"""
        return get_proposal_sessions(proposal_id)
