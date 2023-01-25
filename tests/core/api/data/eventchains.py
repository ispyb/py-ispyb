from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_event_chains = [
    ApiTestElem(
        name="list eventchains empty",
        input=ApiTestInput(
            permissions=[],
            route="/eventchains?dataCollectionId=0",
        ),
        expected=ApiTestExpected(code=200),
    )
]
