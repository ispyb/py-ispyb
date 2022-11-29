from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_proteins_list = [
    ApiTestElem(
        name="List proteins",
        input=ApiTestInput(
            login="abcd",
            route="/proteins",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="Get a protein",
        input=ApiTestInput(
            login="abcd",
            route="/proteins/1",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List proteins (admin)",
        input=ApiTestInput(
            permissions=[
                "bl_admin",
            ],
            login="efgh",
            route="/proteins",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
