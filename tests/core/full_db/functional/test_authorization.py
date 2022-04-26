import pytest
from tests.core.full_db.functional.data.authorization import (
    test_data_session,
    test_data_proposal,
)
from tests.core.utils import get_token


def get_elem_name(test_elem):
    return test_elem["name"]


def _run_authorization_t(ispyb_app, ispyb_settings, test_elem):
    name = test_elem["name"]

    inputs = test_elem["input"]
    permissions = inputs["permissions"]
    username = inputs["username"]
    route = ispyb_settings.api_root + inputs["route"]

    expected = test_elem["expected"]
    code = expected["code"]

    token = get_token(
        ispyb_app, permissions, api_root=ispyb_settings.api_root, user=username
    )

    headers = {"Authorization": "Bearer " + token}

    response = ispyb_app.get(route, headers=headers)
    print(response.json())
    assert response.status_code == code, "[GET] %s " % (name)


@pytest.mark.parametrize("test_elem", test_data_session, ids=get_elem_name)
def test_authorization_session(ispyb_app, ispyb_settings, test_elem):
    _run_authorization_t(ispyb_app, ispyb_settings, test_elem)


@pytest.mark.parametrize("test_elem", test_data_proposal, ids=get_elem_name)
def test_authorization_proposal(ispyb_app, ispyb_settings, test_elem):
    _run_authorization_t(ispyb_app, ispyb_settings, test_elem)
