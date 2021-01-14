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
        'autoProcStatusId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcIntegrationId': f_fields.Integer(required=True, description=''),
        'step': f_fields.String(required=True, description='autoprocessing stepenum(Indexing,Integration,Correction,Scaling,Importing)'),
        'status': f_fields.String(required=True, description='autoprocessing statusenum(Launched,Successful,Failed)'),
        'comments': f_fields.String(required=False, description='comments'),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        }

class AutoProcStatusSchema(Schema):
    """Marshmallows schema class representing AutoProcStatus table"""

    autoProcStatusId = ma_fields.Integer()
    autoProcIntegrationId = ma_fields.Integer()
    step = ma_fields.String()
    status = ma_fields.String()
    comments = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()

f_schema = api.model('AutoProcStatus', dict_schema)
ma_schema = AutoProcStatusSchema()
json_schema = JSONSchema().dump(ma_schema)
