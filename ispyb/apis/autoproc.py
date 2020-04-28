"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

from ispyb import app
from ispyb.auth import token_required
from ispyb.models import AutoProc as AutoProcModel
from ispyb.schemas import f_auto_proc_schema,  ma_auto_proc_schema

ns = Namespace('Auto processing', description='Auto processing related namespace', path='/autoproc')

@ns.route("")
class AutoProcList(Resource):
    """Auto processing resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all auto processing results"""
        app.logger.info('Returns all auto proc results')
        auto_proc_list = AutoProcModel.query.all()
        return ma_auto_proc_schema.dump(auto_proc_list)
