from flask_restx import Namespace, Resource
from app.models import AutoProcProgram as AutoProcProgramModel
from app.modules.auto_proc_program.schemas import (
    f_auto_proc_program_schema,
    ma_auto_proc_program_schema,
)

"""
api = Namespace(
    "AutoProcProgram",
    description="AutoProcProgram related namespace",
    path="/auto_proc_program",
)


@api.route("")
class AutoProcProgramList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_program_list = AutoProcProgramModel.query.all()
        return ma_auto_proc_program_schema.dump(auto_proc_program_list)
"""
