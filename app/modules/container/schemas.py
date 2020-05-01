
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

container_dict = {
        'containerId': f_fields.Integer(required=True, description=''),
        'dewarId': f_fields.Integer(required=False, description=''),
        'code': f_fields.String(required=False, description=''),
        'containerType': f_fields.String(required=False, description=''),
        'capacity': f_fields.Integer(required=False, description=''),
        'beamlineLocation': f_fields.String(required=False, description=''),
        'sampleChangerLocation': f_fields.String(required=False, description=''),
        'containerStatus': f_fields.String(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=False, description=''),
        'barcode': f_fields.String(required=False, description=''),
        'sessionId': f_fields.Integer(required=False, description=''),
        'ownerId': f_fields.Integer(required=False, description=''),
        'screenId': f_fields.Integer(required=False, description=''),
        'scheduleId': f_fields.Integer(required=False, description=''),
        'imagerId': f_fields.Integer(required=False, description=''),
        'scLocationUpdated': f_fields.DateTime(required=False, description=''),
        'requestedImagerId': f_fields.Integer(required=False, description=''),
        'requestedReturn': f_fields.Integer(required=False, description='True for requesting return, False means container will be disposed'),
        'comments': f_fields.String(required=False, description=''),
        'experimentType': f_fields.String(required=False, description=''),
        'storageTemperature': f_fields.Float(required=False, description=''),
        'containerRegistryId': f_fields.Integer(required=False, description=''),
        }

class ContainerSchema(Schema):
    containerId = ma_fields.Integer()
    dewarId = ma_fields.Integer()
    code = ma_fields.String()
    containerType = ma_fields.String()
    capacity = ma_fields.Integer()
    beamlineLocation = ma_fields.String()
    sampleChangerLocation = ma_fields.String()
    containerStatus = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    barcode = ma_fields.String()
    sessionId = ma_fields.Integer()
    ownerId = ma_fields.Integer()
    screenId = ma_fields.Integer()
    scheduleId = ma_fields.Integer()
    imagerId = ma_fields.Integer()
    scLocationUpdated = ma_fields.DateTime()
    requestedImagerId = ma_fields.Integer()
    requestedReturn = ma_fields.Integer()
    comments = ma_fields.String()
    experimentType = ma_fields.String()
    storageTemperature = ma_fields.Float()
    containerRegistryId = ma_fields.Integer()

f_container_schema = api.model('Container', container_dict)
ma_container_schema = ContainerSchema()
