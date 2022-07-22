from fastapi.testclient import TestClient
import pytest

from starlette.types import ASGIApp

from pyispyb.config import settings
from pyispyb.app.main import app as _app
from tests.authclient import AuthClient


@pytest.fixture()
def client():
    return TestClient(_app)


@pytest.fixture
def app() -> ASGIApp:
    yield _app


@pytest.fixture
def auth_client_abcd(client: TestClient):
    auth = AuthClient(client, settings.api_root)
    auth.login(username="abcd", permissions="abcd")
    yield auth


@pytest.fixture
def auth_client_efgh(client: TestClient):
    auth = AuthClient(client, settings.api_root)
    auth.login(username="efgh", permissions="efgh")
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
