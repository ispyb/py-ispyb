import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.admin.activity import test_data_admin_activity


@pytest.mark.parametrize("test_elem", test_data_admin_activity, ids=get_elem_name)
def test_activity_list(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)
