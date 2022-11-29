import requests
import json


class RestClient:
    base = "http://localhost"
    port = 8000
    _token = None

    def __init__(self, base=None, port=None, verify=True):
        if base is not None:
            self.base = base

        if port is not None:
            self.port = port

        self.verify = verify

    def token(self):
        return self._token

    def print(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))

    def req(
        self,
        url,
        method="get",
        data=None,
        params=None,
        pprint=False,
        token=True,
        show_headers=False,
    ):
        parts = self.base.split("/")
        base = (
            parts[0]
            + "/"
            + parts[1]
            + "/"
            + parts[2]
            + ":"
            + str(self.port)
            + "/"
            + "/".join(parts[3:])
        )

        headers = None
        if self._token and token:
            headers = {"Authorization": "Bearer " + self._token}
        resp = getattr(requests, method)(
            base + url,
            json=data,
            params=params,
            headers=headers,
            verify=self.verify,
        )

        if pprint:
            print(resp.url, resp.status_code, len(resp.content))
            if show_headers:
                print(resp.headers)
            try:
                self.print(resp.json())
            except Exception:
                print(resp.text)

            return

        else:
            return resp

    def login(self, login, password):
        auth = {"login": login, "password": password, "plugin": "dummy"}
        resp = self.req("/auth/login", "post", auth)
        if resp.status_code == 201:
            self._token = resp.json()["token"]
            print("permissions: ", resp.json()["permissions"])
        else:
            try:
                print(resp.status_code, resp.json())
            except Exception:
                print(resp.status_code, resp.text)
            return False

        return True
