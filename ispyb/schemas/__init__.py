from ispyb import api

from ispyb.schemas.sample import sample_dict, SampleSchema
f_sample_schema = api.model('Sample', sample_dict)
ma_sample_schema = SampleSchema()

from ispyb.schemas.data_collection import data_collection_dict, DataCollectionSchema
f_data_collection_schema = api.model('DataCollection', data_collection_dict)
ma_data_collection_schema = DataCollectionSchema()

from ispyb.schemas.person import person_dict, PersonSchema
f_person_schema = api.model('Person', person_dict)
ma_person_schema = PersonSchema()

from ispyb.schemas.proposal import proposal_dict, ProposalSchema
f_proposal_schema = api.model('Proposal', proposal_dict)
ma_proposal_schema = ProposalSchema()

