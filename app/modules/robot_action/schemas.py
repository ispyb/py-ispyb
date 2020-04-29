
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api
robot_action_dict = {
        'robotActionId': f_fields.Integer(required=True, description=''),
        'blsessionId': f_fields.Integer(required=True, description=''),
        'blsampleId': f_fields.Integer(required=False, description=''),
        'actionType': f_fields.String(required=False, description='enum(LOAD,UNLOAD,DISPOSE,STORE,WASH,ANNEAL)'),
        'startTimestamp': f_fields.DateTime(required=True, description=''),
        'endTimestamp': f_fields.DateTime(required=True, description=''),
        'status': f_fields.String(required=False, description='enum(SUCCESS,ERROR,CRITICAL,WARNING,COMMANDNOTSENT)'),
        'message': f_fields.String(required=False, description=''),
        'containerLocation': f_fields.Integer(required=False, description=''),
        'dewarLocation': f_fields.Integer(required=False, description=''),
        'sampleBarcode': f_fields.String(required=False, description=''),
        'xtalSnapshotBefore': f_fields.String(required=False, description=''),
        'xtalSnapshotAfter': f_fields.String(required=False, description=''),
        }

class RobotActionSchema(Schema):
    robotActionId = ma_fields.Integer()

    blsessionId = ma_fields.Integer()

    blsampleId = ma_fields.Integer()

    actionType = ma_fields.String()

    startTimestamp = ma_fields.DateTime()

    endTimestamp = ma_fields.DateTime()

    status = ma_fields.String()

    message = ma_fields.String()

    containerLocation = ma_fields.Integer()

    dewarLocation = ma_fields.Integer()

    sampleBarcode = ma_fields.String()

    xtalSnapshotBefore = ma_fields.String()

    xtalSnapshotAfter = ma_fields.String()

f_robot_action_schema = api.model('RobotAction', robot_action_dict)
ma_robot_action_schema = RobotActionSchema()
