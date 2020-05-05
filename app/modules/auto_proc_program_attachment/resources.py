from flask_restx import Namespace, Resource
from app.models import AutoProcProgramAttachment as AutoProcProgramAttachmentModel
from app.modules.auto_proc_program_attachment.schemas import (
    f_auto_proc_program_attachment_schema,
    ma_auto_proc_program_attachment_schema,
)

"""
api = Namespace(
    "AutoProcProgramAttachment",
    description="AutoProcProgramAttachment related namespace",
    path="/auto_proc_program_attachment",
)


@api.route("")
class AutoProcProgramAttachmentList(Resource):
    @api.doc(security="apikey")
    def get(self):
        auto_proc_program_attachment_list = AutoProcProgramAttachmentModel.query.all()
        return ma_auto_proc_program_attachment_schema.dump(
            auto_proc_program_attachment_list
        )
"""
