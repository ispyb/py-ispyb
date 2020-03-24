from ispyb import ma
from ispyb.models.proposal import ProposalModel

class ProposalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProposalModel

    proposalId = ma.auto_field()
    title = ma.auto_field()
    proposalCode = ma.auto_field()
    proposalNumber = ma.auto_field()
