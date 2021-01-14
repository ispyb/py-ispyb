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
        'screeningId': f_fields.Integer(required=True, description=''),
        'dataCollectionId': f_fields.Integer(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        'programVersion': f_fields.String(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'shortComments': f_fields.String(required=False, description=''),
        'diffractionPlanId': f_fields.Integer(required=False, description='references DiffractionPlan'),
        'dataCollectionGroupId': f_fields.Integer(required=False, description=''),
        'xmlSampleInformation': f_fields.String(required=False, description=''),
        }

class ScreeningSchema(Schema):
    """Marshmallows schema class representing Screening table"""

    screeningId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    bltimeStamp = ma_fields.DateTime()
    programVersion = ma_fields.String()
    comments = ma_fields.String()
    shortComments = ma_fields.String()
    diffractionPlanId = ma_fields.Integer()
    dataCollectionGroupId = ma_fields.Integer()
    xmlSampleInformation = ma_fields.String()

f_schema = api.model('Screening', dict_schema)
ma_schema = ScreeningSchema()
json_schema = JSONSchema().dump(ma_schema)
