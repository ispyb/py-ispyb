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
        'containerId': f_fields.Integer(required=True, description=''),
        'dewarId': f_fields.Integer(required=False, description=''),
        'code': f_fields.String(required=False, description=''),
        'containerType': f_fields.String(required=False, description=''),
        'capacity': f_fields.Integer(required=False, description=''),
        'sampleChangerLocation': f_fields.String(required=False, description=''),
        'containerStatus': f_fields.String(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=False, description=''),
        'beamlineLocation': f_fields.String(required=False, description=''),
        'screenId': f_fields.Integer(required=False, description=''),
        'scheduleId': f_fields.Integer(required=False, description=''),
        'barcode': f_fields.String(required=False, description=''),
        'imagerId': f_fields.Integer(required=False, description=''),
        'sessionId': f_fields.Integer(required=False, description=''),
        'ownerId': f_fields.Integer(required=False, description=''),
        'requestedImagerId': f_fields.Integer(required=False, description=''),
        'requestedReturn': f_fields.Integer(required=False, description='True for requesting return, False means container will be disposed'),
        'comments': f_fields.String(required=False, description=''),
        'experimentType': f_fields.String(required=False, description=''),
        'storageTemperature': f_fields.Float(required=False, description=''),
        'containerRegistryId': f_fields.Integer(required=False, description=''),
        }

class ContainerSchema(Schema):
    """Marshmallows schema class representing Container table"""

    containerId = ma_fields.Integer()
    dewarId = ma_fields.Integer()
    code = ma_fields.String()
    containerType = ma_fields.String()
    capacity = ma_fields.Integer()
    sampleChangerLocation = ma_fields.String()
    containerStatus = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    beamlineLocation = ma_fields.String()
    screenId = ma_fields.Integer()
    scheduleId = ma_fields.Integer()
    barcode = ma_fields.String()
    imagerId = ma_fields.Integer()
    sessionId = ma_fields.Integer()
    ownerId = ma_fields.Integer()
    requestedImagerId = ma_fields.Integer()
    requestedReturn = ma_fields.Integer()
    comments = ma_fields.String()
    experimentType = ma_fields.String()
    storageTemperature = ma_fields.Float()
    containerRegistryId = ma_fields.Integer()

f_schema = api.model('Container', dict_schema)
ma_schema = ContainerSchema()
json_schema = JSONSchema().dump(ma_schema)
