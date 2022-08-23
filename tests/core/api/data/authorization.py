from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput

test_data_session = [
    ApiTestElem(
        name="all_sessions permission OK",
        input=ApiTestInput(
            permissions=[
                "all_sessions",
            ],
            login="efgh",
            route="/em/session/70566/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no all_sessions permission DENIED",
        input=ApiTestInput(
            permissions=[],
            login="efgh",
            route="/em/session/70566/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission OK (proposal.personId)",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            login="pasteur",
            route="/em/session/70566/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_sessions permission DENIED (proposal.personId)",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/em/session/70566/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission OK (Session_has_Person.personId)",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            login="darwin",
            route="/em/session/70565/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_sessions permission DENIED (Session_has_Person.personId)",
        input=ApiTestInput(
            permissions=[],
            login="darwin",
            route="/em/session/70565/stats",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_sessions permission DENIED",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            login="abcd",
            route="/em/session/70566/stats",
            method="get",
            payload=None,
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
            login="efgh",
            route="/proposals/MX1",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no all_proposals permission DENIED",
        input=ApiTestInput(
            permissions=[],
            login="efgh",
            route="/proposals/MX1",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_proposals permission OK (proposal.personId)",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            login="pasteur",
            route="/proposals/MX1",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=200),
    ),
    ApiTestElem(
        name="no own_proposals permission DENIED (proposal.personId)",
        input=ApiTestInput(
            permissions=[],
            login="pasteur",
            route="/proposals/MX1",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
    ApiTestElem(
        name="own_proposals permission DENIED",
        input=ApiTestInput(
            permissions=[
                "own_proposals",
            ],
            login="abcd",
            route="/proposals/MX1",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(code=403),
    ),
]
