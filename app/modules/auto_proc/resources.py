"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

from app.models import AutoProc as AutoProcModel
from app.modules.auto_proc.schemas import f_auto_proc_schema,  ma_auto_proc_schema

api = Namespace('Auto processing', description='Auto processing related namespace', path='/autoproc')

@api.route("")
class AutoProcList(Resource):
    """Auto processing resource"""

    @api.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all auto processing results"""
        #app.logger.info('Returns all auto proc results')
        auto_proc_list = AutoProcModel.query.all()
        return ma_auto_proc_schema.dump(auto_proc_list)
