from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_samples_list = [
    ApiTestElem(
        name="List samples",
        input=ApiTestInput(
            login="abcd",
            route="/samples",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List samples (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/samples",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]

test_data_subsamples_list = [
    ApiTestElem(
        name="List sub samples",
        input=ApiTestInput(
            login="abcd",
            route="/samples/sub",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List sub samples (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/samples/sub",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]


test_data_sampleimages_list = [
    ApiTestElem(
        name="List sample images",
        input=ApiTestInput(
            login="abcd",
            route="/samples/images",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List sample images (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/samples/images",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]