from tests import data

from app.schemas.data_collection import DataCollectionSchema
from app.schemas.proposal import ProposalSchema


def test_data_collection_model():
    return
    data_collection = DataCollectionSchema().dump(data.test_data_collection)

    assert data_collection.errors == {}


def test_proposal_model():
    return
    proposal = ProposalSchema().dump(data.test_proposal)

    assert proposal.errors == {}
