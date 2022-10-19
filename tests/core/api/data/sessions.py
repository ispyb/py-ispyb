from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_sessions_list = [
    ApiTestElem(
        name="List sessions",
        input=ApiTestInput(
            login="abcd",
            route="/sessions",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="abcd / blc00001-1 / 200",
        input=ApiTestInput(
            login="abcd",
            route="/sessions/1",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List sessions (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/sessions",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="efgh / blc00001-1 / 404",
        input=ApiTestInput(
            login="efgh",
            permissions=[
                "bl_admin",
            ],
            route="/sessions/1",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
]
