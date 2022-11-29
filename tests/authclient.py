from fastapi import Response
from fastapi.testclient import TestClient


class AuthClient:
    def __init__(self, client: TestClient, base_url: str):
        self._client = client
        self._base_url = base_url

    def login(self, login: str, permissions: str):
        res = self._client.post(
            f"{self._base_url}/auth/login",
            json={"login": login, "password": permissions, "plugin": "dummy"},
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
        payload = kwargs.pop("payload", None)
        if payload is not None:
            return getattr(self._client, method)(
                full_url, json=payload, headers=headers
            )
        else:
            return getattr(self._client, method)(full_url, headers=headers)

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
