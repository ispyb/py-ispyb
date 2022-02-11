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
    'shippingId': f_fields.Integer(required=True, description=''),
    'proposalId': f_fields.Integer(required=True, description=''),
    'shippingName': f_fields.String(required=False, description=''),
    'deliveryAgent_agentName': f_fields.String(required=False, description=''),
    'deliveryAgent_shippingDate': f_fields.String(required=False, description=''),
    'deliveryAgent_deliveryDate': f_fields.String(required=False, description=''),
    'deliveryAgent_agentCode': f_fields.String(required=False, description=''),
    'deliveryAgent_flightCode': f_fields.String(required=False, description=''),
    'shippingStatus': f_fields.String(required=False, description=''),
    'bltimeStamp': f_fields.DateTime(required=False, description=''),
    'laboratoryId': f_fields.Integer(required=False, description=''),
    'isStorageShipping': f_fields.Integer(required=False, description=''),
    'creationDate': f_fields.DateTime(required=False, description=''),
    'comments': f_fields.String(required=False, description=''),
    'sendingLabContactId': f_fields.Integer(required=False, description=''),
    'returnLabContactId': f_fields.Integer(required=False, description=''),
    'returnCourier': f_fields.String(required=False, description=''),
    'dateOfShippingToUser': f_fields.DateTime(required=False, description=''),
    'shippingType': f_fields.String(required=False, description=''),
    'safetyLevel': f_fields.String(required=False, description=''),
}


class ShippingSchema(Schema):
    """Marshmallows schema class representing Shipping table"""

    shippingId = ma_fields.Integer()
    proposalId = ma_fields.Integer()
    shippingName = ma_fields.String()
    deliveryAgent_agentName = ma_fields.String()
    deliveryAgent_shippingDate = ma_fields.String()
    deliveryAgent_deliveryDate = ma_fields.String()
    deliveryAgent_agentCode = ma_fields.String()
    deliveryAgent_flightCode = ma_fields.String()
    shippingStatus = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    laboratoryId = ma_fields.Integer()
    isStorageShipping = ma_fields.Integer()
    creationDate = ma_fields.DateTime()
    comments = ma_fields.String()
    sendingLabContactId = ma_fields.Integer()
    returnLabContactId = ma_fields.Integer()
    returnCourier = ma_fields.String()
    dateOfShippingToUser = ma_fields.DateTime()
    shippingType = ma_fields.String()
    safetyLevel = ma_fields.String()


f_schema = api.model('Shipping', dict_schema)
ma_schema = ShippingSchema()
json_schema = JSONSchema().dump(ma_schema)
