from ispyb.tests import data
from ispyb.models import DataCollection, Proposal

def test_data_collection_model():
    data_collection = DataCollection(**data.test_data_collection)

def test_proposal_model():
    proposal = Proposal(**data.test_proposal)

