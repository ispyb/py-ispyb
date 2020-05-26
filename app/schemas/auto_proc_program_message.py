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

from app.extensions.api import api_v1 as api

auto_proc_program_message_dict = {
        'autoProcProgramMessageId': f_fields.Integer(required=True, description=''),
        'autoProcProgramId': f_fields.Integer(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description=''),
        'severity': f_fields.String(required=False, description='enum(ERROR,WARNING,INFO)'),
        'message': f_fields.String(required=False, description=''),
        'description': f_fields.String(required=False, description=''),
        }

class AutoProcProgramMessageSchema(Schema):
    """Marshmallows schema class representing AutoProcProgramMessage table"""

    autoProcProgramMessageId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()
    severity = ma_fields.String()
    message = ma_fields.String()
    description = ma_fields.String()

f_auto_proc_program_message_schema = api.model('AutoProcProgramMessage', auto_proc_program_message_dict)
ma_auto_proc_program_message_schema = AutoProcProgramMessageSchema()

