"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

auto_proc_status_dict = {
        'autoProcStatusId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcIntegrationId': f_fields.Integer(required=True, description=''),
        'step': f_fields.String(required=True, description='autoprocessing stepenum(Indexing,Integration,Correction,Scaling,Importing)'),
        'status': f_fields.String(required=True, description='autoprocessing statusenum(Launched,Successful,Failed)'),
        'comments': f_fields.String(required=False, description='comments'),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        }

class AutoProcStatusSchema(Schema):
    """Marshmallows schema class representing AutoProcStatus table"""

    autoProcStatusId = ma_fields.Integer()
    autoProcIntegrationId = ma_fields.Integer()
    step = ma_fields.String()
    status = ma_fields.String()
    comments = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()

f_auto_proc_status_schema = api.model('AutoProcStatus', auto_proc_status_dict)
ma_auto_proc_status_schema = AutoProcStatusSchema()

