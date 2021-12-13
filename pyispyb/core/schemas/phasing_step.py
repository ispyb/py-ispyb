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
        'phasingStepId': f_fields.Integer(required=True, description=''),
        'previousPhasingStepId': f_fields.Integer(required=False, description=''),
        'programRunId': f_fields.Integer(required=False, description=''),
        'spaceGroupId': f_fields.Integer(required=False, description=''),
        'autoProcScalingId': f_fields.Integer(required=False, description=''),
        'phasingAnalysisId': f_fields.Integer(required=False, description=''),
        'phasingStepType': f_fields.String(required=False, description='enum(PREPARE,SUBSTRUCTUREDETERMINATION,PHASING,MODELBUILDING,REFINEMENT,LIGAND_FIT)'),
        'method': f_fields.String(required=False, description=''),
        'solventContent': f_fields.String(required=False, description=''),
        'enantiomorph': f_fields.String(required=False, description=''),
        'lowRes': f_fields.String(required=False, description=''),
        'highRes': f_fields.String(required=False, description=''),
        'groupName': f_fields.String(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description=''),
        }

class PhasingStepSchema(Schema):
    """Marshmallows schema class representing PhasingStep table"""

    phasingStepId = ma_fields.Integer()
    previousPhasingStepId = ma_fields.Integer()
    programRunId = ma_fields.Integer()
    spaceGroupId = ma_fields.Integer()
    autoProcScalingId = ma_fields.Integer()
    phasingAnalysisId = ma_fields.Integer()
    phasingStepType = ma_fields.String()
    method = ma_fields.String()
    solventContent = ma_fields.String()
    enantiomorph = ma_fields.String()
    lowRes = ma_fields.String()
    highRes = ma_fields.String()
    groupName = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()

f_schema = api.model('PhasingStep', dict_schema)
ma_schema = PhasingStepSchema()
json_schema = JSONSchema().dump(ma_schema)
