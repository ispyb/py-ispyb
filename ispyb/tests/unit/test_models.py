from ispyb.models import Proposal as ProposalModel

def test_new_proposal():
    proposal_dict = {
            "proposalCode": "MX",
            "title": "Test proposal",
            "proposalType": "MX",
            "personId": 1,
            "proposalId": 1,
            "externalId": None,
            "proposalNumber": "1",
            "bltimeStamp": "2015-12-21 16:20:43",
            "state": "Open"
            }
    proposal = ProposalModel(**proposal_dict)

