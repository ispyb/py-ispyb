# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from app.extensions.api import api_v1 as api

micrograph_dict_schema = {
    "micrographId": f_fields.Integer(required=True, description=""),
    "url": f_fields.String(required=False, description=""),
    "objectSidePixelSize": f_fields.String(
        required=False, description="comma separated two floats"
    ),
    "description": f_fields.String(required=False, description=""),
}


class MicrographSchema(Schema):
    """Marshmallows schema class representing Micrograph table"""

    micrographId = ma_fields.Integer()
    url = ma_fields.String()
    objectSidePixelSize = ma_fields.String()
    description = ma_fields.String()


micrograph_f_schema = api.model("Micrograph", micrograph_dict_schema)
micrograph_ma_schema = MicrographSchema()
micrograph_json_schema = JSONSchema().dump(micrograph_ma_schema)
