import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.admin.options import test_data_options


@pytest.mark.parametrize("test_elem", test_data_options, ids=get_elem_name)
def test_get_options(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


def test_post_option(auth_client_abcd: AuthClient):
    response = auth_client_abcd.patch("/options")

    assert response.status_code == 403
