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
    'phasingHasScalingId': f_fields.Integer(
        required=True,
        description='Primary key (auto-incremented)'),
    'phasingAnalysisId': f_fields.Integer(
        required=True,
        description='Related phasing analysis item'),
    'autoProcScalingId': f_fields.Integer(
        required=True,
        description='Related autoProcScaling item'),
    'datasetNumber': f_fields.Integer(
        required=False,
        description='serial number of the dataset and always reserve 0 for the reference'),
    'recordTimeStamp': f_fields.DateTime(
        required=True,
        description=''),
}


class Phasing_has_ScalingSchema(Schema):
    """Marshmallows schema class representing Phasing_has_Scaling table"""

    phasingHasScalingId = ma_fields.Integer()
    phasingAnalysisId = ma_fields.Integer()
    autoProcScalingId = ma_fields.Integer()
    datasetNumber = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()


f_schema = api.model('Phasing_has_Scaling', dict_schema)
ma_schema = Phasing_has_ScalingSchema()
json_schema = JSONSchema().dump(ma_schema)
