from flask_restx import Namespace, Resource
from app.models import AutoProcProgramMessage as AutoProcProgramMessageModel
from app.modules.auto_proc_program_message.schemas import (
    f_auto_proc_program_message_schema,
    ma_auto_proc_program_message_schema,
)

api = Namespace(
    "AutoProcProgramMessage",
    description="AutoProcProgramMessage related namespace",
    path="/auto_proc_program_message",
)


@api.route("")
class AutoProcProgramMessageList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_program_message_list = AutoProcProgramMessageModel.query.all()
        return ma_auto_proc_program_message_schema.dump(auto_proc_program_message_list)
