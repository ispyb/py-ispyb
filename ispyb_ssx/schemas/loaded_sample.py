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
    "loadedSampleId": f_fields.Integer(required=True, description=""),
    "name": f_fields.String(
        required=False,
        description="to be used as part of the image and processing file names",
    ),
    "sampleStockId": f_fields.Integer(required=False, description=""),
    "sampleDeliveryDeviceId": f_fields.Integer(required=False, description=""),
    "loadingPattern": f_fields.Integer(required=False, description=""),
    "descriptionJson": f_fields.String(required=False, description=""),
}


class LoadedSampleSchema(Schema):
    """Marshmallows schema class representing LoadedSample table"""

    loadedSampleId = ma_fields.Integer()
    name = ma_fields.String()
    sampleStockId = ma_fields.Integer()
    sampleDeliveryDeviceId = ma_fields.Integer()
    loadingPattern = ma_fields.Integer()
    descriptionJson = ma_fields.String()


f_schema = api.model("LoadedSample", dict_schema)
ma_schema = LoadedSampleSchema()
json_schema = JSONSchema().dump(ma_schema)
