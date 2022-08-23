from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_events = [
    ApiTestElem(
        name="list events",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/events",
            method="get",
            payload=None,
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
