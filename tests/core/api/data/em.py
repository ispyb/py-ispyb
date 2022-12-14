from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_em_list = [
    ApiTestElem(
        name="List movies",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/em/movies",
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
]

test_em_fft = [
    ApiTestElem(
        name="Get FFT thumbnail",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/em/movie/1/thumbnail/fft",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
]

test_em_micrograph = [
    ApiTestElem(
        name="Get micrograph snapshot",
        input=ApiTestInput(
            permissions=[],
            login="abcd",
            route="/em/movie/1/snapshot/micrograph",
        ),
        expected=ApiTestExpected(
            code=404,
        ),
    ),
]
