from starlette.types import ASGIApp

from tests.core.api.utils.permissions import mock_permissions
from tests.authclient import AuthClient


def test_all_proposals(auth_client_efgh: AuthClient, app: ASGIApp):
    """Browse all proposals"""
    with mock_permissions("all_proposals", app):
        resp = auth_client_efgh.get("/proposals")
        assert resp.status_code == 200
        json = resp.json()

        assert len(json["results"]) == 3


def test_bl_admin(auth_client_efgh: AuthClient, app: ASGIApp, with_beamline_groups):
    """Should be able to browse proposals on beamline id00"""
    with mock_permissions("bl_admin", app):
        resp = auth_client_efgh.get("/proposals")
        assert resp.status_code == 200
        json = resp.json()

        assert len(json["results"]) == 1
        assert json["results"][0]["_metadata"]["beamlines"] == ["id00"]


def test_no_permission(auth_client_abcd: AuthClient):
    """Browse only proposals with SessionHasPerson links"""
    resp = auth_client_abcd.get("/proposals")
    assert resp.status_code == 200
    json = resp.json()

    assert len(json["results"]) == 1
    assert json["results"][0]["_metadata"]["beamlines"] == ["bl"]