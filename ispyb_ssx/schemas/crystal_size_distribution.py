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

crystal_size_distribution_dict_schema = {
    "crystalSizeDistributionId": f_fields.Integer(required=True, description=""),
    "crystalHabit": f_fields.String(required=False, description=""),
    "characteristicDimensions": f_fields.Float(required=False, description=""),
    "minDimension": f_fields.String(
        required=False, description="comma separated floats"
    ),
    "maxDimension": f_fields.Float(
        required=False, description="comma separated floats"
    ),
}


class CrystalSizeDistributionSchema(Schema):
    """Marshmallows schema class representing CrystalSizeDistribution table"""

    crystalSizeDistributionId = ma_fields.Integer()
    crystalHabit = ma_fields.String()
    characteristicDimensions = ma_fields.Float()
    minDimension = ma_fields.String()
    maxDimension = ma_fields.Float()


crystal_size_distribution_f_schema = api.model(
    "CrystalSizeDistribution", crystal_size_distribution_dict_schema
)
crystal_size_distribution_ma_schema = CrystalSizeDistributionSchema()
crystal_size_distribution_json_schema = JSONSchema().dump(
    crystal_size_distribution_ma_schema
)
