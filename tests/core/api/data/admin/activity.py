from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_admin_activity = [
    ApiTestElem(
        name="list admin activity",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/admin/activity",
        ),
        expected=ApiTestExpected(
            code=403,
        ),
    ),
    ApiTestElem(
        name="list admin activity",
        input=ApiTestInput(
            permissions=["view_activity"],
            login="abcd",
            route="/admin/activity",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
