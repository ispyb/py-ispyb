from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_proposal_list = [
    ApiTestElem(
        name="List proposals",
        input=ApiTestInput(
            login="abcd",
            route="/proposals",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="abcd / MX1 / 404",
        input=ApiTestInput(
            login="abcd",
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
    ApiTestElem(
        name="List proposals (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/proposals",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="efgh / MX1 / 200",
        input=ApiTestInput(
            login="efgh",
            permissions=[
                "bl_admin",
            ],
            route="/proposals/MX1",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="efgh / blc00001 / 404",
        input=ApiTestInput(
            login="efgh",
            permissions=[
                "bl_admin",
            ],
            route="/proposals/blc00001",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
]
