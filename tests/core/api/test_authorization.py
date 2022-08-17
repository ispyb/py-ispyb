import pytest

from starlette.types import ASGIApp

from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem

from tests.core.api.data.authorization import (
    test_data_session,
    test_data_proposal,
)


@pytest.mark.parametrize("test_elem", test_data_session, ids=get_elem_name)
def test_authorization_session(
    auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp
):
    run_test(auth_client, test_elem, app)


@pytest.mark.parametrize("test_elem", test_data_proposal, ids=get_elem_name)
def test_authorization_proposal(
    auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp
):
    run_test(auth_client, test_elem, app)
