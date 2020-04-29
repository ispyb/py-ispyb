from flask_restx import Namespace, Resource
from app.models import AutoProcScaling as AutoProcScalingModel
from app.modules.auto_proc_scaling.schemas import f_auto_proc_scaling_schema,  ma_auto_proc_scaling_schema

api = Namespace('AutoProcScaling', description='AutoProcScaling related namespace', path='/auto_proc_scaling')

@api.route("")
class AutoProcScalingList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_scaling_list = AutoProcScalingModel.query.all()
        return ma_auto_proc_scaling_schema.dump(auto_proc_scaling_list)
