import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem
from tests.core.api.data.em import test_em_fft, test_em_list, test_em_micrograph


@pytest.mark.parametrize("test_elem", test_em_list, ids=get_elem_name)
def test_em_list(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_em_fft, ids=get_elem_name)
def test_em_fft(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_em_micrograph, ids=get_elem_name)
def test_em_micrograph(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)
