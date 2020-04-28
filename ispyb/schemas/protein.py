
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

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
        'global': f_fields.Integer(required=False, description=''),
        }

class ProteinSchema(Schema):
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
