from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_options = [
    ApiTestElem(
        name="list ui options",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/options/ui",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="list all options",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/options",
        ),
        expected=ApiTestExpected(
            code=403,
        ),
    ),
    ApiTestElem(
        name="list all options",
        input=ApiTestInput(
            permissions=["manage_options"],
            login="abcd",
            route="/options",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
