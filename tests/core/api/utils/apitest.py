from typing import Any

from starlette.types import ASGIApp

from tests.authclient import AuthClient
from jsondiff import diff

from tests.core.api.utils.permissions import mock_permissions


class ApiTestInput:
    def __init__(
        self,
        login: str,
        permissions: list[str],
        route: str,
        method: str = "get",
        payload: str | None = None,
    ) -> None:
        self.login = login
        self.permissions = permissions
        self.route = route
        self.method = method
        self.payload = payload


class ApiTestExpected:
    def __init__(
        self, code: int | None = None, res: dict[str, Any] | None = None
    ) -> None:
        self.code = code
        self.res = res


class ApiTestElem:
    def __init__(
        self, name: str, input: ApiTestInput, expected: ApiTestExpected
    ) -> None:
        self.name = name
        self.input = input
        self.expected = expected


def get_elem_name(test_elem: ApiTestElem):
    return test_elem.name


def run_test(auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp):
    with mock_permissions(test_elem.input.permissions, app):
        auth_client.login(test_elem.input.login, "password")

        if test_elem.input.method == "get":
            response = auth_client.get(test_elem.input.route)
        elif test_elem.input.method == "post":
            response = auth_client.post(
                test_elem.input.route, payload=test_elem.input.payload
            )

        if test_elem.expected.code is not None:
            assert (
                response.status_code == test_elem.expected.code
            ), f"""
            TEST { test_elem.name }
            EXPECTED code { test_elem.expected.code }
            GOT code { response.status_code }
            """

        if test_elem.expected.res is not None:
            assert (
                response.json() == test_elem.expected.res
            ), f"""
            TEST { test_elem.name }

            EXPECTED json
            =============================
            { test_elem.expected.res }
            =============================

            GOT json
            =============================
            { response.json() }
            =============================
            
            DIFF
            =============================
            { diff(test_elem.expected.res, response.json()) }
            =============================
            """
