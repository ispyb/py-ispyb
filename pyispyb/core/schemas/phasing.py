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
        'phasingId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'phasingAnalysisId': f_fields.Integer(required=True, description='Related phasing analysis item'),
        'phasingProgramRunId': f_fields.Integer(required=True, description='Related program item'),
        'spaceGroupId': f_fields.Integer(required=False, description='Related spaceGroup'),
        'method': f_fields.String(required=False, description='phasing methodenum(solvent flattening,solvent flipping)'),
        'solventContent': f_fields.String(required=False, description=''),
        'enantiomorph': f_fields.Integer(required=False, description='0 or 1'),
        'lowRes': f_fields.String(required=False, description=''),
        'highRes': f_fields.String(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description=''),
        }

class PhasingSchema(Schema):
    """Marshmallows schema class representing Phasing table"""

    phasingId = ma_fields.Integer()
    phasingAnalysisId = ma_fields.Integer()
    phasingProgramRunId = ma_fields.Integer()
    spaceGroupId = ma_fields.Integer()
    method = ma_fields.String()
    solventContent = ma_fields.String()
    enantiomorph = ma_fields.Integer()
    lowRes = ma_fields.String()
    highRes = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()

f_schema = api.model('Phasing', dict_schema)
ma_schema = PhasingSchema()
json_schema = JSONSchema().dump(ma_schema)
