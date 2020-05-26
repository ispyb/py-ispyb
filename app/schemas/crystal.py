"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

crystal_dict = {
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
        'packingFraction': f_fields.Float(required=False, description=''),
        'theoreticaldensity': f_fields.Float(required=False, description=''),
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
    packingFraction = ma_fields.Float()
    theoreticaldensity = ma_fields.Float()

f_crystal_schema = api.model('Crystal', crystal_dict)
ma_crystal_schema = CrystalSchema()

