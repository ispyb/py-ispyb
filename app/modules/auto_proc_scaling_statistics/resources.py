from flask_restx import Namespace, Resource
from app.models import AutoProcScalingStatistic as AutoProcScalingStatisticsModel
from app.modules.auto_proc_scaling_statistics.schemas import (
    f_auto_proc_scaling_statistics_schema,
    ma_auto_proc_scaling_statistics_schema,
)

api = Namespace(
    "AutoProcScalingStatistics",
    description="AutoProcScalingStatistics related namespace",
    path="/auto_proc_scaling_statistics",
)


@api.route("")
class AutoProcScalingStatisticsList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_scaling_statistics_list = AutoProcScalingStatisticsModel.query.all()
        return ma_auto_proc_scaling_statistics_schema.dump(
            auto_proc_scaling_statistics_list
        )
