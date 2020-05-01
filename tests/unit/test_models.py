from tests import data
from app.modules.proposal.schemas import ProposalSchema

#def test_data_collection_model():
#    data_collection = DataCollection(**data.test_data_collection)

def test_proposal_model():
    ma_proposal_schema = ProposalSchema(**data.test_proposal)

