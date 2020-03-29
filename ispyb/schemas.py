from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields
from ispyb import api


class ProposalSchema(Schema):
    proposalId = ma_fields.Int()
    title = ma_fields.Str()
    proposalCode = ma_fields.Str()
    proposalNumber = ma_fields.Str()
    bltimeStamp = ma_fields.DateTime()
    proposalType = ma_fields.Str()
    externalId = ma_fields.Int()
    state = ma_fields.Str()

proposal_schema = api.model('Proposal', {
    'proposalId': fields.Integer(required=True, description='Proposal id as integer'),
    'title': fields.String(),
    'proposalCode': fields.String(description='MX, BX'),
    'proposalNumber': fields.String(),
    'bltimeStamp': fields.DateTime,
    'proposalType': fields.String(),
    'externalId': fields.Integer(),
    'state': fields.String(),
    }
    )
