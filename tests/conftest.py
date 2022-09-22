from fastapi.testclient import TestClient
import pytest

from starlette.types import ASGIApp
from pyispyb.app.extensions.database.middleware import get_session
from pyispyb.config import settings
from pyispyb.app.main import app as _app
from tests.authclient import AuthClient
from tests.core.api.utils.permissions import mock_permissions


@pytest.fixture()
def client():
    return TestClient(_app)


@pytest.fixture
def app() -> ASGIApp:
    yield _app


@pytest.fixture
def with_db_session():
    with get_session() as db_session:
        yield db_session


@pytest.fixture
def auth_client_abcd(client: TestClient):
    auth = AuthClient(client, settings.api_root)
    auth.login(login="abcd", permissions="abcd")
    yield auth


@pytest.fixture
def auth_client_efgh(client: TestClient):
    auth = AuthClient(client, settings.api_root)
    auth.login(login="efgh", permissions="efgh")
    yield auth


@pytest.fixture
def auth_client(client: TestClient):
    auth = AuthClient(client, settings.api_root)
    yield auth


@pytest.fixture
def short_session():
    old_token_exp_time = settings.token_exp_time

    new_token_exp_time = 0
    settings.token_exp_time = new_token_exp_time

    yield new_token_exp_time
    settings.token_exp_time = old_token_exp_time


@pytest.fixture
def with_beamline_groups(auth_client_efgh: AuthClient, app: ASGIApp):
    with mock_permissions(["manage_options"], app):
        resp = auth_client_efgh.post(
            "/options",
            payload={
                "beamlineGroups": [
                    {
                        "groupName": "BL0x",
                        "uiGroup": "mx",
                        "permission": "bl_admin",
                        "beamlines": [
                            {"beamlineName": "BL01"},
                            {"beamlineName": "BL02"},
                        ],
                    },
                ]
            },
        )

        assert resp.status_code == 200

        yield
