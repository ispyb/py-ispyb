from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput

test_data_session = [
    ApiTestElem(
        name="all_sessions permission OK",
        input=ApiTestInput(
            permissions=[
                "all_sessions",
            ],
            username="admin",
            route="/em/session/70566/stats",
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no all_sessions permission DENIED",
        input=ApiTestInput(
            permissions=["none"],
            username="admin",
            route="/em/session/70566/stats",
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission OK (proposal.personId)",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/em/session/70566/stats",
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_sessions permission DENIED (proposal.personId)",
        input=ApiTestInput(
            permissions=["none"],
            username="70565",
            route="/em/session/70566/stats",
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission OK (Session_has_Person.personId)",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="darwin",
            route="/em/session/70565/stats",
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_sessions permission DENIED (Session_has_Person.personId)",
        input=ApiTestInput(
            permissions=[
                "none",
            ],
            username="darwin",
            route="/em/session/70565/stats",
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission DENIED",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="user",
            route="/em/session/70566/stats",
        ),
        expected=ApiTestExpected(code=403),
    ),
]

test_data_proposal = [
    ApiTestElem(
        name="all_proposals permission OK",
        input=ApiTestInput(
            permissions=[
                "all_proposals",
            ],
            username="admin",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no all_proposals permission DENIED",
        input=ApiTestInput(
            permissions=["none"],
            username="admin",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_proposals permission OK (proposal.personId)",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="pasteur",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_proposals permission DENIED (proposal.personId)",
        input=ApiTestInput(
            permissions=["none"],
            username="pasteur",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_proposals permission DENIED",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            username="user",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(code=403),
    ),
]
