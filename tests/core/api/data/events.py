from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_events = [
    ApiTestElem(
        name="list events",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/events",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="get event types",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/events/types",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
