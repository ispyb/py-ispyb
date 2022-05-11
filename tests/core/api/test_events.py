from tests.conftest import AuthClient


def test_events(auth_client_abcd: AuthClient):
    res = auth_client_abcd.get("/events")
    assert res.status_code == 200
