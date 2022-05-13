from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_events = [
    ApiTestElem(
        name="list events",
        input=ApiTestInput(
            permissions=[],
            username="abc",
            route="/events",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
