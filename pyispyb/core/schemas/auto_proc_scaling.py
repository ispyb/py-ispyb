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
        'autoProcScalingId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcId': f_fields.Integer(required=False, description='Related autoProc item (used by foreign key)'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        }

class AutoProcScalingSchema(Schema):
    """Marshmallows schema class representing AutoProcScaling table"""

    autoProcScalingId = ma_fields.Integer()
    autoProcId = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()

f_schema = api.model('AutoProcScaling', dict_schema)
ma_schema = AutoProcScalingSchema()
json_schema = JSONSchema().dump(ma_schema)
