from marshmallow import Schema, fields

class ProposalSchema(Schema):
    proposalId = fields.Int()
    title = fields.Str()
    proposalCode = fields.Str()
    proposalNumber = fields.Str()

