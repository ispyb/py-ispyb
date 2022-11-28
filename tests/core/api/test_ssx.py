import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.ssx import (
    test_data_ssx_stats,
    test_data_ssx_cells,
    test_data_ssx_histogram,
)


@pytest.mark.parametrize("test_elem", test_data_ssx_stats, ids=get_elem_name)
def test_ssx_stats(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_ssx_cells, ids=get_elem_name)
def test_ssx_cells(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_ssx_histogram, ids=get_elem_name)
def test_ssx_histogram(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    run_test(auth_client, test_elem, app)
