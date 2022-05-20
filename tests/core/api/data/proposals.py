from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput

test_data_proposal_list = [
    ApiTestElem(
        name="list own_proposals",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="pasteur",
            route="/proposals",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "Proposal_proposalId": 9096,
                    "Proposal_proposalType": "MX",
                    "Proposal_personId": 404290,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_proposalNumber": "1",
                }
            ],
        ),
    ),
    ApiTestElem(
        name="empty list own_proposals",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="i_dont_have_proposals",
            route="/proposals",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
    ApiTestElem(
        name="list all_proposals",
        input=ApiTestInput(
            permissions=[
                "all_proposals",
            ],
            username="pasteur",
            route="/proposals",
        ),
        expected=ApiTestExpected(code=200),
    ),
]

test_data_proposal_info = [
    ApiTestElem(
        name="own_proposals OK proposal name",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="pasteur",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(
            code=200,
            res={
                "proposal": {
                    "proposalId": 9096,
                    "proposalCode": "MX",
                    "proposalType": "MX",
                    "externalId": None,
                    "personId": 404290,
                    "title": "TEST",
                    "proposalNumber": "1",
                    "bltimeStamp": "2022-05-10T07:59:31",
                    "state": "Open",
                }
            },
        ),
    ),
    ApiTestElem(
        name="own_proposals OK proposal id",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="pasteur",
            route="/proposals/9096",
        ),
        expected=ApiTestExpected(
            code=200,
            res={
                "proposal": {
                    "proposalId": 9096,
                    "proposalCode": "MX",
                    "proposalType": "MX",
                    "externalId": None,
                    "personId": 404290,
                    "title": "TEST",
                    "proposalNumber": "1",
                    "bltimeStamp": "2022-05-10T07:59:31",
                    "state": "Open",
                }
            },
        ),
    ),
    ApiTestElem(
        name="own_proposals NOK",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="i_dont_have_proposals",
            route="/proposals/9096",
        ),
        expected=ApiTestExpected(
            code=403,
            res={
                "detail": "User i_dont_have_proposals (permissions assigned: ['own_proposals']) is not authorized to access proposal 9096."
            },
        ),
    ),
    ApiTestElem(
        name="invalid proposal",
        input=ApiTestInput(
            permissions=[
                "all_proposals",
            ],
            username="pasteur",
            route="/proposals/NOT_A_VALID_PROPOSAL",
        ),
        expected=ApiTestExpected(
            code=200,
            res={"proposal": None},
        ),
    ),
]
