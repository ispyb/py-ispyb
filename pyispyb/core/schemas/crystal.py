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
        'crystalId': f_fields.Integer(required=True, description=''),
        'diffractionPlanId': f_fields.Integer(required=False, description=''),
        'proteinId': f_fields.Integer(required=True, description=''),
        'crystalUUID': f_fields.String(required=False, description=''),
        'name': f_fields.String(required=False, description=''),
        'spaceGroup': f_fields.String(required=False, description=''),
        'morphology': f_fields.String(required=False, description=''),
        'color': f_fields.String(required=False, description=''),
        'size_X': f_fields.String(required=False, description=''),
        'size_Y': f_fields.String(required=False, description=''),
        'size_Z': f_fields.String(required=False, description=''),
        'cell_a': f_fields.String(required=False, description=''),
        'cell_b': f_fields.String(required=False, description=''),
        'cell_c': f_fields.String(required=False, description=''),
        'cell_alpha': f_fields.String(required=False, description=''),
        'cell_beta': f_fields.String(required=False, description=''),
        'cell_gamma': f_fields.String(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'pdbFileName': f_fields.String(required=False, description='pdb file name'),
        'pdbFilePath': f_fields.String(required=False, description='pdb file path'),
        'recordTimeStamp': f_fields.DateTime(required=True, description='Creation or last update date/time'),
        'abundance': f_fields.Float(required=False, description=''),
        'theoreticalDensity': f_fields.Float(required=False, description=''),
        }

class CrystalSchema(Schema):
    """Marshmallows schema class representing Crystal table"""

    crystalId = ma_fields.Integer()
    diffractionPlanId = ma_fields.Integer()
    proteinId = ma_fields.Integer()
    crystalUUID = ma_fields.String()
    name = ma_fields.String()
    spaceGroup = ma_fields.String()
    morphology = ma_fields.String()
    color = ma_fields.String()
    size_X = ma_fields.String()
    size_Y = ma_fields.String()
    size_Z = ma_fields.String()
    cell_a = ma_fields.String()
    cell_b = ma_fields.String()
    cell_c = ma_fields.String()
    cell_alpha = ma_fields.String()
    cell_beta = ma_fields.String()
    cell_gamma = ma_fields.String()
    comments = ma_fields.String()
    pdbFileName = ma_fields.String()
    pdbFilePath = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    abundance = ma_fields.Float()
    theoreticalDensity = ma_fields.Float()

f_schema = api.model('Crystal', dict_schema)
ma_schema = CrystalSchema()
json_schema = JSONSchema().dump(ma_schema)
