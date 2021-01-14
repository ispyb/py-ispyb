"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"



from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

dict_schema = {
        'robotActionId': f_fields.Integer(required=True, description=''),
        'blsessionId': f_fields.Integer(required=True, description=''),
        'blsampleId': f_fields.Integer(required=False, description=''),
        'actionType': f_fields.String(required=False, description='enum(LOAD,UNLOAD,DISPOSE,STORE,WASH,ANNEAL)'),
        'startTimestamp': f_fields.DateTime(required=True, description=''),
        'endTimestamp': f_fields.DateTime(required=True, description=''),
        'status': f_fields.String(required=False, description='enum(SUCCESS,ERROR,CRITICAL,WARNING,EPICSFAIL,COMMANDNOTSENT)'),
        'message': f_fields.String(required=False, description=''),
        'containerLocation': f_fields.Integer(required=False, description=''),
        'dewarLocation': f_fields.Integer(required=False, description=''),
        'sampleBarcode': f_fields.String(required=False, description=''),
        'xtalSnapshotBefore': f_fields.String(required=False, description=''),
        'xtalSnapshotAfter': f_fields.String(required=False, description=''),
        }

class RobotActionSchema(Schema):
    """Marshmallows schema class representing RobotAction table"""

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

f_schema = api.model('RobotAction', dict_schema)
ma_schema = RobotActionSchema()
json_schema = JSONSchema().dump(ma_schema)
