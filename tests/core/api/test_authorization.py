from typing import Any
import pytest

from tests.core.api.data.authorization import (
    test_data_session,
    test_data_proposal,
)

from tests.conftest import AuthClient


def get_elem_name(test_elem: dict[str, Any]):
    return test_elem["name"]


def _run_authorization_t(auth_client: AuthClient, test_elem: dict[str, Any]):
    name = test_elem["name"]

    inputs = test_elem["input"]
    permissions = inputs["permissions"]
    username = inputs["username"]
    route = inputs["route"]

    expected = test_elem["expected"]
    code = expected["code"]

    auth_client.login(username, ",".join(permissions))

    response = auth_client.get(route)
    print(response.json())
    assert response.status_code == code, "[GET] %s " % (name)


@pytest.mark.parametrize("test_elem", test_data_session, ids=get_elem_name)
def test_authorization_session(auth_client: AuthClient, test_elem: dict[str, Any]):
    _run_authorization_t(auth_client, test_elem)


@pytest.mark.parametrize("test_elem", test_data_proposal, ids=get_elem_name)
def test_authorization_proposal(auth_client: AuthClient, test_elem: dict[str, Any]):
    _run_authorization_t(auth_client, test_elem)
