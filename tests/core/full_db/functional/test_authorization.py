
import pytest
from tests.core.full_db.functional.data.authorization import test_data_session, test_data_proposal
from tests.core.utils import get_token


def get_elem_name(test_elem):
    return test_elem["name"]


def _run_authorization_t(ispyb_app, test_elem):
    name = test_elem["name"]

    input = test_elem["input"]
    permissions = input["permissions"]
    username = input["username"]
    route = ispyb_app.config["API_ROOT"] + input["route"]

    expected = test_elem["expected"]
    code = expected["code"]

    token = get_token(ispyb_app, permissions, user=username)

    client = ispyb_app.test_client()
    headers = {"Authorization": "Bearer " + token}

    response = client.get(route, headers=headers)
    print(response.json)
    assert response.status_code == code, "[GET] %s " % (name)


@pytest.mark.parametrize("test_elem", test_data_session, ids=get_elem_name)
def test_authorization_session(ispyb_app, test_elem):
    _run_authorization_t(ispyb_app, test_elem)


@pytest.mark.parametrize("test_elem", test_data_proposal, ids=get_elem_name)
def test_authorization_proposal(ispyb_app, test_elem):
    _run_authorization_t(ispyb_app, test_elem)
