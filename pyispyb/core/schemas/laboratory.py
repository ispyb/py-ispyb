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
        'laboratoryId': f_fields.Integer(required=True, description=''),
        'laboratoryUUID': f_fields.String(required=False, description=''),
        'name': f_fields.String(required=False, description=''),
        'address': f_fields.String(required=False, description=''),
        'city': f_fields.String(required=False, description=''),
        'country': f_fields.String(required=False, description=''),
        'url': f_fields.String(required=False, description=''),
        'organization': f_fields.String(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description='Creation or last update date/time'),
        'laboratoryPk': f_fields.Integer(required=False, description=''),
        'postcode': f_fields.String(required=False, description=''),
        }

class LaboratorySchema(Schema):
    """Marshmallows schema class representing Laboratory table"""

    laboratoryId = ma_fields.Integer()
    laboratoryUUID = ma_fields.String()
    name = ma_fields.String()
    address = ma_fields.String()
    city = ma_fields.String()
    country = ma_fields.String()
    url = ma_fields.String()
    organization = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    laboratoryPk = ma_fields.Integer()
    postcode = ma_fields.String()

f_schema = api.model('Laboratory', dict_schema)
ma_schema = LaboratorySchema()
json_schema = JSONSchema().dump(ma_schema)
