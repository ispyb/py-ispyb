"""
Project: py-ispyb
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

from app.extensions.api import api_v1 as api

dict_schema = {
        'sampleStockId': f_fields.Integer(required=True, description=''),
        'name': f_fields.String(required=True, description=''),
        'crystalSlurryId': f_fields.Integer(required=True, description=''),
        'concentrationFactor': f_fields.Float(required=True, description=''),
        'crystalDensity': f_fields.Float(required=True, description=''),
        'additiveId': f_fields.Integer(required=False, description='reference to Additive.additiveId'),
        'note': f_fields.String(required=False, description=''),
        }

class SampleStockSchema(Schema):
    """Marshmallows schema class representing SampleStock table"""

    sampleStockId = ma_fields.Integer()
    name = ma_fields.String()
    crystalSlurryId = ma_fields.Integer()
    concentrationFactor = ma_fields.Float()
    crystalDensity = ma_fields.Float()
    additiveId = ma_fields.Integer()
    note = ma_fields.String()

f_schema = api.model('SampleStock', dict_schema)
ma_schema = SampleStockSchema()
json_schema = JSONSchema().dump(ma_schema)
