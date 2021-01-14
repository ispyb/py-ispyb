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

timed_sequence_dict_schema = {
    "timedSequenceId": f_fields.Integer(required=True, description=""),
    "name": f_fields.String(required=False, description=""),
    "timeOn": f_fields.Float(required=False, description="sec"),
    "timeOff": f_fields.Float(required=False, description="sec"),
    "nameInShortlist": f_fields.String(required=False, description=""),
    "triggerDevice": f_fields.String(required=False, description=""),
}


class TimedSequenceSchema(Schema):
    """Marshmallows schema class representing TimedSequence table"""

    timedSequenceId = ma_fields.Integer()
    name = ma_fields.String()
    timeOn = ma_fields.Float()
    timeOff = ma_fields.Float()
    nameInShortlist = ma_fields.String()
    triggerDevice = ma_fields.String()


timed_sequence_f_schema = api.model("TimedSequence", timed_sequence_dict_schema)
timed_sequence_ma_schema = TimedSequenceSchema()
timed_sequence_json_schema = JSONSchema().dump(timed_sequence_ma_schema)
