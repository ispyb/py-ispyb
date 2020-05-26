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

protein_dict = {
        'proteinId': f_fields.Integer(required=True, description=''),
        'proposalId': f_fields.Integer(required=True, description=''),
        'name': f_fields.String(required=False, description=''),
        'acronym': f_fields.String(required=False, description=''),
        'safetyLevel': f_fields.String(required=False, description='enum(GREEN,YELLOW,RED)'),
        'molecularMass': f_fields.String(required=False, description=''),
        'proteinType': f_fields.String(required=False, description=''),
        'sequence': f_fields.String(required=False, description=''),
        'personId': f_fields.Integer(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        'isCreatedBySampleSheet': f_fields.Integer(required=False, description=''),
        'externalId': f_fields.Integer(required=False, description=''),
        'density': f_fields.Float(required=False, description=''),
        'componentTypeId': f_fields.Integer(required=False, description=''),
        'modId': f_fields.String(required=False, description=''),
        'concentrationTypeId': f_fields.Integer(required=False, description=''),
        'Global': f_fields.Integer(required=False, description=''),
        }

class ProteinSchema(Schema):
    """Marshmallows schema class representing Protein table"""

    proteinId = ma_fields.Integer()
    proposalId = ma_fields.Integer()
    name = ma_fields.String()
    acronym = ma_fields.String()
    safetyLevel = ma_fields.String()
    molecularMass = ma_fields.String()
    proteinType = ma_fields.String()
    sequence = ma_fields.String()
    personId = ma_fields.Integer()
    bltimeStamp = ma_fields.DateTime()
    isCreatedBySampleSheet = ma_fields.Integer()
    externalId = ma_fields.Integer()
    density = ma_fields.Float()
    componentTypeId = ma_fields.Integer()
    modId = ma_fields.String()
    concentrationTypeId = ma_fields.Integer()
    Global = ma_fields.Integer()

f_protein_schema = api.model('Protein', protein_dict)
ma_protein_schema = ProteinSchema()

