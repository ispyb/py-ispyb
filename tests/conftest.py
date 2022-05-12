from fastapi.testclient import TestClient
import pytest

from tests.appsettings import app, settings
from tests.authclient import AuthClient


@pytest.fixture()
def client():
    return TestClient(app)


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
