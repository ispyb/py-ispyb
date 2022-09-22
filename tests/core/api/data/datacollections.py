from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_dc_attachments = [
    ApiTestElem(
        name="List dc attachments",
        input=ApiTestInput(
            login="abcd",
            route="/datacollections/attachments",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List dc attachments (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/datacollections/attachments",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]

test_dc_images = [
    ApiTestElem(
        name="Get datacollection image",
        input=ApiTestInput(
            login="abcd",
            route="/datacollections/images/1",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
    ApiTestElem(
        name="Get datacollection image (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/datacollections/images/1",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
]
