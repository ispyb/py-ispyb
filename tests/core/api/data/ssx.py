from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_ssx_stats = [
    ApiTestElem(
        name="list stats empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/stats?dataCollectionIds=1,2",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
    ApiTestElem(
        name="list stats wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/stats?dataCollectionIds=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]

test_data_ssx_cells = [
    ApiTestElem(
        name="cells empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells?dataCollectionId=1",
        ),
        expected=ApiTestExpected(code=404),
    ),
    ApiTestElem(
        name="list stats wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells?dataCollectionId=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]


test_data_ssx_histogram = [
    ApiTestElem(
        name="histogram empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells/histogram?dataCollectionIds=1,2",
        ),
        expected=ApiTestExpected(
            code=200,
            res={
                "a": None,
                "b": None,
                "c": None,
                "alpha": None,
                "beta": None,
                "gamma": None,
            },
        ),
    ),
    ApiTestElem(
        name="histogram wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells/histogram?dataCollectionIds=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]
