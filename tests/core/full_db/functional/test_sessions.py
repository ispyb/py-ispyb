
import pytest
from tests.core.full_db.functional.data.sessions import test_data_session_proposal_list, test_data_session_list, test_data_session_dates_list
from tests.core.utils import get_token


def get_elem_name(test_elem):
    return test_elem["name"]


def _run_session_t(ispyb_app, test_elem):
    name = test_elem["name"]

    inputs = test_elem["input"]
    permissions = inputs["permissions"]
    username = inputs["username"]
    route = ispyb_app.config["API_ROOT"] + inputs["route"]

    expected = test_elem["expected"]
    code = expected["code"]
    res = expected["res"]

    token = get_token(ispyb_app, permissions, user=username)

    client = ispyb_app.test_client()
    headers = {"Authorization": "Bearer " + token}

    response = client.get(route, headers=headers)
    print(response.json)
    assert response.status_code == code, "[GET] %s " % (name)
    assert response.json == res, "[GET] %s " % (name)


@pytest.mark.parametrize("test_elem",
                         test_data_session_list,
                         ids=get_elem_name)
def test_session_list(ispyb_app, test_elem):
    _run_session_t(ispyb_app, test_elem)


@pytest.mark.parametrize("test_elem",
                         test_data_session_dates_list,
                         ids=get_elem_name)
def test_session_dates_list(ispyb_app, test_elem):
    _run_session_t(ispyb_app, test_elem)


@pytest.mark.parametrize("test_elem",
                         test_data_session_proposal_list,
                         ids=get_elem_name)
def test_session_proposal_list(ispyb_app, test_elem):
    _run_session_t(ispyb_app, test_elem)
