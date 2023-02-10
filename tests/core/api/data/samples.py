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
        name="Get a samples",
        input=ApiTestInput(
            login="abcd",
            route="/samples/1",
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
        name="Get a sub sample",
        input=ApiTestInput(
            login="abcd",
            route="/samples/sub/2",
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
        name="Get sample image",
        input=ApiTestInput(
            login="abcd",
            route="/samples/images/1",
        ),
        expected=ApiTestExpected(
            code=404,
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

test_data_create_sample = [
    ApiTestElem(
        name="Create minimal sample",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "crystalId": 1,
                },
                "sample_compositions": [],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="Create sample with new crystal basic",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "Protein": {"proteinId": 1},
                    "crystal_compositions": [],
                },
                "sample_compositions": [],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="Create sample with new crystal with composition",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "Protein": {"proteinId": 1},
                    "crystal_compositions": [
                        {
                            "Component": {
                                "name": "a",
                                "composition": "test",
                                "ComponentType": {
                                    "name": "Buffer",
                                },
                            },
                            "abundance": "1",
                        }
                    ],
                },
                "sample_compositions": [],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="Create sample unknown crystal",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "crystalId": -1,
                },
                "sample_compositions": [],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
    ApiTestElem(
        name="Create sample unknown protein",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "Protein": {"proteinId": -1},
                    "crystal_compositions": [],
                },
                "sample_compositions": [],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
    ApiTestElem(
        name="Create sample with composition",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "crystalId": 1,
                },
                "sample_compositions": [
                    {
                        "Component": {
                            "name": "a",
                            "composition": "test",
                            "ComponentType": {
                                "name": "Buffer",
                            },
                        },
                        "abundance": "1",
                    }
                ],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="Create sample with unknown component",
        input=ApiTestInput(
            route="/samples",
            method="post",
            payload={
                "name": "test sample",
                "Crystal": {
                    "crystalId": 1,
                },
                "sample_compositions": [
                    {
                        "Component": {"componentId": -1},
                        "abundance": "1",
                    }
                ],
                "loopType": "Injector",
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
]

test_data_components = [
    ApiTestElem(
        name="List components",
        input=ApiTestInput(
            route="/samples/components",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List component types",
        input=ApiTestInput(
            route="/samples/components/types",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="List component types",
        input=ApiTestInput(
            route="/samples/concentration/types",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]
