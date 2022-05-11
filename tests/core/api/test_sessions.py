import pytest
from tests.core.api.data.sessions import (
    test_data_session_proposal_list,
    test_data_session_list,
    test_data_session_dates_list,
)
from typing import Any
from tests.conftest import AuthClient


def get_elem_name(test_elem):
    return test_elem["name"]


def _run_session_t(auth_client: AuthClient, test_elem: dict[str, Any]):
    name = test_elem["name"]

    inputs = test_elem["input"]
    permissions = inputs["permissions"]
    username = inputs["username"]
    route = inputs["route"]

    expected = test_elem["expected"]
    code = expected["code"]
    res = expected["res"]

    auth_client.login(username, ",".join(permissions))

    response = auth_client.get(route)
    print(response.json())

    assert response.status_code == code, "[GET] %s " % (name)
    assert response.json() == res, "[GET] %s " % (name)


@pytest.mark.parametrize("test_elem", test_data_session_list, ids=get_elem_name)
def test_session_list(auth_client: AuthClient, test_elem: dict[str, Any]):
    _run_session_t(auth_client, test_elem)


@pytest.mark.parametrize("test_elem", test_data_session_dates_list, ids=get_elem_name)
def test_session_dates_list(auth_client: AuthClient, test_elem: dict[str, Any]):
    _run_session_t(auth_client, test_elem)


@pytest.mark.parametrize(
    "test_elem", test_data_session_proposal_list, ids=get_elem_name
)
def test_session_proposal_list(auth_client: AuthClient, test_elem: dict[str, Any]):
    _run_session_t(auth_client, test_elem)
