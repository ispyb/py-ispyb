
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

auto_proc_program_attachment_dict = {
        'autoProcProgramAttachmentId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcProgramId': f_fields.Integer(required=True, description='Related autoProcProgram item'),
        'fileType': f_fields.String(required=False, description='Type of file Attachmentenum(Log,Result,Graph)'),
        'fileName': f_fields.String(required=False, description='Attachment filename'),
        'filePath': f_fields.String(required=False, description='Attachment filepath to disk storage'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        }

class AutoProcProgramAttachmentSchema(Schema):
    autoProcProgramAttachmentId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    fileType = ma_fields.String()
    fileName = ma_fields.String()
    filePath = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
