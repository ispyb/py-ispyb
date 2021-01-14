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
        'personId': f_fields.Integer(required=True, description=''),
        'laboratoryId': f_fields.Integer(required=False, description=''),
        'siteId': f_fields.Integer(required=False, description=''),
        'personUUID': f_fields.String(required=False, description=''),
        'familyName': f_fields.String(required=False, description=''),
        'givenName': f_fields.String(required=False, description=''),
        'title': f_fields.String(required=False, description=''),
        'emailAddress': f_fields.String(required=False, description=''),
        'phoneNumber': f_fields.String(required=False, description=''),
        'login': f_fields.String(required=False, description=''),
        'faxNumber': f_fields.String(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description='Creation or last update date/time'),
        'cache': f_fields.String(required=False, description=''),
        'externalId': f_fields.Integer(required=False, description=''),
        }

class PersonSchema(Schema):
    """Marshmallows schema class representing Person table"""

    personId = ma_fields.Integer()
    laboratoryId = ma_fields.Integer()
    siteId = ma_fields.Integer()
    personUUID = ma_fields.String()
    familyName = ma_fields.String()
    givenName = ma_fields.String()
    title = ma_fields.String()
    emailAddress = ma_fields.String()
    phoneNumber = ma_fields.String()
    login = ma_fields.String()
    faxNumber = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    cache = ma_fields.String()
    externalId = ma_fields.Integer()

f_schema = api.model('Person', dict_schema)
ma_schema = PersonSchema()
json_schema = JSONSchema().dump(ma_schema)
