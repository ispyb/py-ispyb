from marshmallow import Schema, fields


class ProposalSchema(Schema):
    proposalId = fields.Int()
    title = fields.Str()
    proposalCode = fields.Str()
    proposalNumber = fields.Str()
    bltimeStamp = fields.DateTime()
    proposalType = fields.Str()
    externalId = fields.Int()
    state = fields.Str()
