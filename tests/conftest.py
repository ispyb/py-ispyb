from fastapi import Response
from fastapi.testclient import TestClient
import pytest

from tests.appsettings import app, settings


class AuthClient:
    def __init__(self, client: TestClient, base_url: str):
        self._client = client
        self._base_url = base_url

    def login(self, username: str, permissions: str):
        res = self._client.post(
            f"{self._base_url}/auth/login",
            json={"username": username, "password": permissions, "plugin": "dummy"},
        )

        assert res.status_code == 201

        self._token: str = res.json()["token"]
        return res

    def client(
        self, method: str, url: str, *args, use_base_url=True, **kwargs
    ) -> Response:
        headers = {"Authorization": f"Bearer {self._token}"}
        full_url = url
        if use_base_url:
            full_url = self._base_url + url
        return getattr(self._client, method)(
            full_url, json=kwargs.get("payload"), headers=headers
        )

    @property
    def token(self):
        return self._token

    def get(self, *args, **kwargs):
        return self.client("get", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.client("post", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.client("put", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.client("patch", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.client("delete", *args, **kwargs)


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
