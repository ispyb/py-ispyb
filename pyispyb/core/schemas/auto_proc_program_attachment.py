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
        'autoProcProgramAttachmentId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcProgramId': f_fields.Integer(required=True, description='Related autoProcProgram item'),
        'fileType': f_fields.String(required=False, description='Type of file Attachmentenum(Log,Result,Graph,Debug)'),
        'fileName': f_fields.String(required=False, description='Attachment filename'),
        'filePath': f_fields.String(required=False, description='Attachment filepath to disk storage'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        'importanceRank': f_fields.Integer(required=False, description='For the particular autoProcProgramId and fileType, indicate the importance of the attachment. Higher numbers are more important'),
        }

class AutoProcProgramAttachmentSchema(Schema):
    """Marshmallows schema class representing AutoProcProgramAttachment table"""

    autoProcProgramAttachmentId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    fileType = ma_fields.String()
    fileName = ma_fields.String()
    filePath = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    importanceRank = ma_fields.Integer()

f_schema = api.model('AutoProcProgramAttachment', dict_schema)
ma_schema = AutoProcProgramAttachmentSchema()
json_schema = JSONSchema().dump(ma_schema)
