from ispyb import ma, db
from ispyb.models.proposal import ProposalModel
from marshmallow import Schema, fields


class ProposalSchema(Schema):
    proposalId = fields.Int()
    title = fields.Str()
    proposalCode = fields.Str()
    proposalNumber = fields.Str()





'''
class ProposalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProposalModel

    proposalId = ma.auto_field()
    title = ma.auto_field()
    proposalCode = ma.auto_field()
    proposalNumber = ma.auto_field()
'''

