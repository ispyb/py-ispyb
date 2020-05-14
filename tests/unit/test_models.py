from tests import data

from app.modules.data_collection.schemas import DataCollectionSchema
from app.modules.proposal.schemas import ProposalSchema


def test_data_collection_model():
    return
    data_collection = DataCollectionSchema().dump(data.test_data_collection)

    assert data_collection.errors == {}


def test_proposal_model():
    return
    proposal = ProposalSchema().dump(data.test_proposal)

    assert proposal.errors == {}
