from app.models import BLSession as SessionModel
from app.modules.session.schemas import f_session_schema, ma_session_schema


def get_all_sessions():
    session_list = SessionModel.query.all()
    return ma_session_schema.dump(session_list, many=True)


def get_proposal_sessions(proposal_id):
    session_list = SessionModel.query.filter_by(proposalId=proposal_id)
    return ma_session_schema.dump(session_list, many=True)

