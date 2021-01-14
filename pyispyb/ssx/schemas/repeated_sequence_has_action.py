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

from pyispyb.app.extensions.api import api_v1 as api

repeated_sequence_has_action_dict_schema = {
    "repeatedSequenceHasActionId": f_fields.Integer(required=True, description=""),
    "repeatedSequenceId": f_fields.Integer(required=False, description=""),
    "timedExcitationId": f_fields.Integer(required=False, description=""),
    "timedXrayExposureId": f_fields.Integer(required=False, description=""),
    "timedXrayDetectionId": f_fields.Integer(required=False, description=""),
}


class RepeatedSequenceHasActionSchema(Schema):
    """Marshmallows schema class representing RepeatedSequenceHasAction table"""

    repeatedSequenceHasActionId = ma_fields.Integer()
    repeatedSequenceId = ma_fields.Integer()
    timedExcitationId = ma_fields.Integer()
    timedXrayExposureId = ma_fields.Integer()
    timedXrayDetectionId = ma_fields.Integer()


repeated_sequence_has_action_f_schema = api.model(
    "RepeatedSequenceHasAction", repeated_sequence_has_action_dict_schema
)
repeated_sequence_has_action_ma_schema = RepeatedSequenceHasActionSchema()
repeated_sequence_has_action_json_schema = JSONSchema().dump(
    repeated_sequence_has_action_ma_schema
)
