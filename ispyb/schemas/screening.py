
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

screening_dict = {
        'screeningId': f_fields.Integer(required=True, description=''),
        'diffractionPlanId': f_fields.Integer(required=False, description='references DiffractionPlan'),
        'dataCollectionGroupId': f_fields.Integer(required=False, description=''),
        'dataCollectionId': f_fields.Integer(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        'programVersion': f_fields.String(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'shortComments': f_fields.String(required=False, description=''),
        'xmlSampleInformation': f_fields.String(required=False, description=''),
        }

class ScreeningSchema(Schema):
    screeningId = ma_fields.Integer()
    diffractionPlanId = ma_fields.Integer()
    dataCollectionGroupId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    bltimeStamp = ma_fields.DateTime()
    programVersion = ma_fields.String()
    comments = ma_fields.String()
    shortComments = ma_fields.String()
    xmlSampleInformation = ma_fields.String()
