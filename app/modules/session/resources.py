from flask_restx import Namespace, Resource
from app.models import BLSession as SessionModel
from app.modules.session.schemas import f_session_schema,  ma_session_schema

api = Namespace('Session', description='Session related namespace', path='/session')

@api.route("")
class SessionList(Resource):
    @api.doc(security="apikey")
    def get(self):
        session_list = SessionModel.query.all()
        return ma_session_schema.dump(session_list)
