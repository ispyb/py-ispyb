import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.samples import (
    test_data_samples_list,
    test_data_sampleimages_list,
    test_data_subsamples_list,
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
