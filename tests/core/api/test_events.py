def test_events(auth_client):
    res = auth_client.get("/events")
    assert res.status_code == 200
