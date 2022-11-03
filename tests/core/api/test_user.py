from starlette.types import ASGIApp

from tests.authclient import AuthClient


def test_user(auth_client_efgh: AuthClient, app: ASGIApp):
    """Get current user"""
    resp = auth_client_efgh.get("/user/current")
    assert resp.status_code == 200
