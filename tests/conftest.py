import os
from fastapi.testclient import TestClient
import pytest


class AuthClient:
    def __init__(self, client, base_url):
        self._client = client
        self._base_url = base_url

    def login(self, username="abcd", password="abcd"):
        res = self._client.post(
            f"{self._base_url}/auth/login",
            json={"username": username, "password": password, "plugin": "dummy"},
        )

        assert res.status_code == 201

        self._token = res.json()["token"]
        return res

    def client(self, method, url, *args, use_base_url=True, **kwargs):
        headers = {"Authorization": f"Bearer {self._token}"}
        full_url = url
        if use_base_url:
            full_url = self._base_url + url
        print("BASE URL", full_url)
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
def setup_env():
    os.environ["SECRET_KEY"] = "test_secret"
    os.environ[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://test:test@127.0.0.1/test"
    os.environ["ISPYB_AUTH"] = "tests/config/auth.yml"


@pytest.fixture()
def client(setup_env, settings):
    from pyispyb.app.main import app

    return TestClient(app)


@pytest.fixture()
def settings():
    from pyispyb.config import settings

    yield settings


@pytest.fixture
def auth_client(client, settings):
    auth = AuthClient(client, settings.api_root)
    auth.login()
    yield auth


@pytest.fixture
def auth_client_admin(client, settings):
    auth = AuthClient(client, settings.api_root)
    auth.login(username="efgh")
    yield auth


@pytest.fixture
def short_session():
    from pyispyb.config import settings

    old_token_exp_time = settings.token_exp_time

    new_token_exp_time = 3 / 60
    settings.token_exp_time = new_token_exp_time

    yield new_token_exp_time
    settings.token_exp_time = old_token_exp_time
