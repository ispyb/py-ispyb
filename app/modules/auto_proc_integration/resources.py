from flask_restx import Namespace, Resource
from app.models import AutoProcIntegration as AutoProcIntegrationModel
from app.modules.auto_proc_integration.schemas import f_auto_proc_integration_schema,  ma_auto_proc_integration_schema

api = Namespace('AutoProcIntegration', description='AutoProcIntegration related namespace', path='/auto_proc_integration')

@api.route("")
class AutoProcIntegrationList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_integration_list = AutoProcIntegrationModel.query.all()
        return ma_auto_proc_integration_schema.dump(auto_proc_integration_list)
