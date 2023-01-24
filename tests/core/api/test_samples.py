import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.samples import (
    test_data_samples_list,
    test_data_sampleimages_list,
    test_data_subsamples_list,
    test_data_create_sample,
    test_data_components,
)


@pytest.mark.parametrize("test_elem", test_data_samples_list, ids=get_elem_name)
def test_samples_list(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_sampleimages_list, ids=get_elem_name)
def test_sample_images(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_subsamples_list, ids=get_elem_name)
def test_subsamples_list(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_create_sample, ids=get_elem_name)
def test_sample_create(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_components, ids=get_elem_name)
def test_components(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


def test_sample_create_delete(auth_client: AuthClient):
    auth_client.login("abcd", "password")

    sample_response = auth_client.post(
        "/samples",
        payload={
            "name": "test sample",
            "Crystal": {
                "crystalId": 1,
            },
            "sample_compositions": [],
            "loopType": "Injector",
        },
    )
    assert sample_response.status_code == 200

    assert "blSampleId" in sample_response.json()

    sampleId = sample_response.json()["blSampleId"]

    get_response = auth_client.get(f"/samples/{sampleId}")
    assert get_response.status_code == 200

    assert "blSampleId" in get_response.json()
    assert get_response.json()["blSampleId"] == sampleId

    delete_response = auth_client.delete(
        f"/samples/{sampleId}",
    )
    assert delete_response.status_code == 200

    get_response = auth_client.get(f"/samples/{sampleId}")
    assert get_response.status_code == 404
