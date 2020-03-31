from ispyb import api
from ispyb.schemas.data_collection import data_collection_dict, DataCollectionSchema
from ispyb.schemas.proposal import proposal_dict, ProposalSchema


ma_data_collection_schema = DataCollectionSchema()
ma_data_collection_schema = DataCollectionSchema(many=True)
f_data_collection_schema = api.model('Data collection', data_collection_dict)

ma_proposal_schema = ProposalSchema()
ma_proposals_schema = ProposalSchema(many=True)
f_proposal_schema = api.model('Proposal', proposal_dict)
