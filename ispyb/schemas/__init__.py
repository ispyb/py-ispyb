from ispyb import api
from ispyb.schemas.data_collection import data_collection_dict, DataCollectionSchema
from ispyb.schemas.person import person_dict, PersonSchema
from ispyb.schemas.proposal import proposal_dict, ProposalSchema


ma_data_collection_schema = DataCollectionSchema()
f_data_collection_schema = api.model('Data collection', data_collection_dict)

ma_person_schema = PersonSchema()
f_person_schema = api.model('Person', person_dict)

ma_proposal_schema = ProposalSchema()
f_proposal_schema = api.model('Proposal', proposal_dict)
