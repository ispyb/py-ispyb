
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

proposal_dict = {
        'proposalId': f_fields.Integer(),
        'personId': f_fields.Integer(),
        'title': f_fields.String(),
        'proposalCode': f_fields.String(),
        'proposalNumber': f_fields.String(),
        'bltimeStamp': f_fields.DateTime(),
        'proposalType': f_fields.String(),
        'externalId': f_fields.Integer(),
        'state': f_fields.String(),
        }

class ProposalSchema(Schema):
    proposalId = ma_fields.Integer()
    personId = ma_fields.Integer()
    title = ma_fields.String()
    proposalCode = ma_fields.String()
    proposalNumber = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    proposalType = ma_fields.String()
    externalId = ma_fields.Integer()
    state = ma_fields.String()
