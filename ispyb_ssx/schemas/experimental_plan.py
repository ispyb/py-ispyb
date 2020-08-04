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

experimental_plan_dict_schema = {
    "experimentalPlanId": f_fields.Integer(required=True, description=""),
    "name": f_fields.String(required=False, description=""),
    "numberOfRepetitions": f_fields.Integer(
        required=False, description="for micro-fluidic, jet, tape but not for chip"
    ),
    "period": f_fields.Float(
        required=False, description="seconds but unknown/self adjusting for chip"
    ),
    "masterTriggerId": f_fields.Integer(required=False, description=""),
    "repeatedSequenceId": f_fields.Integer(required=True, description=""),
}


class ExperimentalPlanSchema(Schema):
    """Marshmallows schema class representing ExperimentalPlan table"""

    experimentalPlanId = ma_fields.Integer()
    name = ma_fields.String()
    numberOfRepetitions = ma_fields.Integer()
    period = ma_fields.Float()
    masterTriggerId = ma_fields.Integer()
    repeatedSequenceId = ma_fields.Integer()


experimental_plan_f_schema = api.model(
    "ExperimentalPlan", experimental_plan_dict_schema
)
experimental_plan_ma_schema = ExperimentalPlanSchema()
experimental_plan_json_schema = JSONSchema().dump(experimental_plan_ma_schema)
