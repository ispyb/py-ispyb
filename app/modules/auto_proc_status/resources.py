from flask_restx import Namespace, Resource

from app.models import AutoProcStatus as AutoProcStatusModel
from app.modules.auto_proc_status.schemas import (
    f_auto_proc_status_schema,
    ma_auto_proc_status_schema,
)

"""
api = Namespace(
    "AutoProcStatus",
    description="AutoProcStatus related namespace",
    path="/auto_proc_status",
)


@api.route("")
class AutoProcStatusList(Resource):

    @api.doc(security="apikey")
    def get(self):
        auto_proc_status_list = AutoProcStatusModel.query.all()
        return ma_auto_proc_status_schema.dump(auto_proc_status_list)
"""
