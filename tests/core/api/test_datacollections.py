import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.datacollections import test_data_dc_attachments, test_dc_images


@pytest.mark.parametrize("test_elem", test_data_dc_attachments, ids=get_elem_name)
def test_dc_attachments(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_dc_images, ids=get_elem_name)
def test_dc_images(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)
