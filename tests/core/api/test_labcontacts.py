import time

from starlette.types import ASGIApp

from tests.authclient import AuthClient

LABCONTACT = {
    "proposalId": 1,
    "cardName": f"test card {time.time()}",
    "Person": {
        "givenName": "test person",
        "familyName": "last name",
        "Laboratory": {
            "name": "lab name",
            "address": "address",
            "city": "city",
            "country": "country",
        },
    },
}

UPDATED_CONTACT = {"cardName": f"updated card {time.time()}"}


def test_labcontacts(auth_client_abcd: AuthClient, app: ASGIApp):
    """Browse lab contacts"""
    resp = auth_client_abcd.get("/labcontacts")
    assert resp.status_code == 200


def test_create_labcontact(auth_client_abcd: AuthClient, app: ASGIApp):
    """Create a lab contact"""

    resp = auth_client_abcd.post("/labcontacts", payload=LABCONTACT)
    assert resp.status_code == 201


def test_create_labcontact_invalid_proposal(auth_client_efgh: AuthClient, app: ASGIApp):
    """Create a lab contact without valid proposal"""

    resp = auth_client_efgh.post("/labcontacts", payload=LABCONTACT)
    assert resp.status_code == 404


def test_update_labcontact(auth_client_abcd: AuthClient, app: ASGIApp):
    """Browse lab contacts"""
    resp = auth_client_abcd.get("/labcontacts")
    assert resp.status_code == 200

    json = resp.json()
    results = json["results"]
    latest = results[-1]

    resp = auth_client_abcd.patch(
        f"/labcontacts/{latest['labContactId']}", payload=UPDATED_CONTACT
    )
    assert resp.status_code == 200
    updated_json = resp.json()
    assert updated_json["cardName"] == UPDATED_CONTACT["cardName"]
