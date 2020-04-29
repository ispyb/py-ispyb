
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api
auto_proc_program_message_dict = {
        'autoProcProgramMessageId': f_fields.Integer(required=True, description=''),
        'autoProcProgramId': f_fields.Integer(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description=''),
        'severity': f_fields.String(required=False, description='enum(ERROR,WARNING,INFO)'),
        'message': f_fields.String(required=False, description=''),
        'description': f_fields.String(required=False, description=''),
        }

class AutoProcProgramMessageSchema(Schema):
    autoProcProgramMessageId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()
    severity = ma_fields.String()
    message = ma_fields.String()
    description = ma_fields.String()
f_auto_proc_program_message_schema = api.model('AutoProcProgramMessage', auto_proc_program_message_dict)
ma_auto_proc_program_message_schema = AutoProcProgramMessageSchema()
