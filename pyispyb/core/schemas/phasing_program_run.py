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
        'phasingProgramRunId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'phasingCommandLine': f_fields.String(required=False, description='Command line for phasing'),
        'phasingPrograms': f_fields.String(required=False, description='Phasing programs (comma separated)'),
        'phasingStatus': f_fields.Integer(required=False, description='success (1) / fail (0)'),
        'phasingMessage': f_fields.String(required=False, description='warning, error,...'),
        'phasingStartTime': f_fields.DateTime(required=False, description='Processing start time'),
        'phasingEndTime': f_fields.DateTime(required=False, description='Processing end time'),
        'phasingEnvironment': f_fields.String(required=False, description='Cpus, Nodes,...'),
        'recordTimeStamp': f_fields.DateTime(required=False, description=''),
        }

class PhasingProgramRunSchema(Schema):
    """Marshmallows schema class representing PhasingProgramRun table"""

    phasingProgramRunId = ma_fields.Integer()
    phasingCommandLine = ma_fields.String()
    phasingPrograms = ma_fields.String()
    phasingStatus = ma_fields.Integer()
    phasingMessage = ma_fields.String()
    phasingStartTime = ma_fields.DateTime()
    phasingEndTime = ma_fields.DateTime()
    phasingEnvironment = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()

f_schema = api.model('PhasingProgramRun', dict_schema)
ma_schema = PhasingProgramRunSchema()
json_schema = JSONSchema().dump(ma_schema)
