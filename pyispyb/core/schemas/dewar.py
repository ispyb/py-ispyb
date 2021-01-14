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
        'dewarId': f_fields.Integer(required=True, description=''),
        'shippingId': f_fields.Integer(required=False, description=''),
        'code': f_fields.String(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'storageLocation': f_fields.String(required=False, description=''),
        'dewarStatus': f_fields.String(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=False, description=''),
        'isStorageDewar': f_fields.Integer(required=False, description=''),
        'barCode': f_fields.String(required=False, description=''),
        'firstExperimentId': f_fields.Integer(required=False, description=''),
        'customsValue': f_fields.Integer(required=False, description=''),
        'transportValue': f_fields.Integer(required=False, description=''),
        'trackingNumberToSynchrotron': f_fields.String(required=False, description=''),
        'trackingNumberFromSynchrotron': f_fields.String(required=False, description=''),
        'type': f_fields.String(required=True, description='enum(Dewar,Toolbox)'),
        'FACILITYCODE': f_fields.String(required=False, description=''),
        'weight': f_fields.Float(required=False, description='dewar weight in kg'),
        'deliveryAgent_barcode': f_fields.String(required=False, description='Courier piece barcode (not the airway bill)'),
        }

class DewarSchema(Schema):
    """Marshmallows schema class representing Dewar table"""

    dewarId = ma_fields.Integer()
    shippingId = ma_fields.Integer()
    code = ma_fields.String()
    comments = ma_fields.String()
    storageLocation = ma_fields.String()
    dewarStatus = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    isStorageDewar = ma_fields.Integer()
    barCode = ma_fields.String()
    firstExperimentId = ma_fields.Integer()
    customsValue = ma_fields.Integer()
    transportValue = ma_fields.Integer()
    trackingNumberToSynchrotron = ma_fields.String()
    trackingNumberFromSynchrotron = ma_fields.String()
    type = ma_fields.String()
    FACILITYCODE = ma_fields.String()
    weight = ma_fields.Float()
    deliveryAgent_barcode = ma_fields.String()

f_schema = api.model('Dewar', dict_schema)
ma_schema = DewarSchema()
json_schema = JSONSchema().dump(ma_schema)
