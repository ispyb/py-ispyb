
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api
auto_proc_dict = {
        'autoProcId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcProgramId': f_fields.Integer(required=False, description='Related program item'),
        'spaceGroup': f_fields.String(required=False, description='Space group'),
        'refinedCell_a': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_b': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_c': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_alpha': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_beta': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_gamma': f_fields.Float(required=False, description='Refined cell'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        }

class AutoProcSchema(Schema):
    autoProcId = ma_fields.Integer()

    autoProcProgramId = ma_fields.Integer()

    spaceGroup = ma_fields.String()

    refinedCell_a = ma_fields.Float()

    refinedCell_b = ma_fields.Float()

    refinedCell_c = ma_fields.Float()

    refinedCell_alpha = ma_fields.Float()

    refinedCell_beta = ma_fields.Float()

    refinedCell_gamma = ma_fields.Float()

    recordTimeStamp = ma_fields.DateTime()

f_auto_proc_schema = api.model('AutoProc', auto_proc_dict)
ma_auto_proc_schema = AutoProcSchema()
