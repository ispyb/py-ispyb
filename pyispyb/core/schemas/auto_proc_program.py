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
        'autoProcProgramId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'processingCommandLine': f_fields.String(required=False, description='Command line for running the automatic processing'),
        'processingPrograms': f_fields.String(required=False, description='Processing programs (comma separated)'),
        'processingStatus': f_fields.Integer(required=False, description='success (1) / fail (0)'),
        'processingMessage': f_fields.String(required=False, description='warning, error,...'),
        'processingStartTime': f_fields.DateTime(required=False, description='Processing start time'),
        'processingEndTime': f_fields.DateTime(required=False, description='Processing end time'),
        'processingEnvironment': f_fields.String(required=False, description='Cpus, Nodes,...'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        'processingJobId': f_fields.Integer(required=False, description=''),
        'dataCollectionId': f_fields.Integer(required=False, description=''),
        }

class AutoProcProgramSchema(Schema):
    """Marshmallows schema class representing AutoProcProgram table"""

    autoProcProgramId = ma_fields.Integer()
    processingCommandLine = ma_fields.String()
    processingPrograms = ma_fields.String()
    processingStatus = ma_fields.Integer()
    processingMessage = ma_fields.String()
    processingStartTime = ma_fields.DateTime()
    processingEndTime = ma_fields.DateTime()
    processingEnvironment = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    processingJobId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()

f_schema = api.model('AutoProcProgram', dict_schema)
ma_schema = AutoProcProgramSchema()
json_schema = JSONSchema().dump(ma_schema)
