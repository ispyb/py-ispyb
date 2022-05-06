import time


def test_token_create_decode(client, settings):
    res = client.post(
        f"{settings.api_root}/auth/login",
        json={"username": "abcd", "password": "abcd", "plugin": "dummy"},
    )
    assert res.status_code == 201

    headers = {"Authorization": f"Bearer {res.json()['token']}"}
    res2 = client.get(f"{settings.api_root}/events", headers=headers)
    assert res2.status_code == 200


def test_token_expired(settings, short_session, client):
    res = client.post(
        f"{settings.api_root}/auth/login",
        json={"username": "abcd", "password": "abcd", "plugin": "dummy"},
    )
    assert res.status_code == 201

    time.sleep(short_session * 60 + 1)

    headers = {"Authorization": f"Bearer {res.json()['token']}"}
    res2 = client.get(f"{settings.api_root}/events", headers=headers)
    assert res2.status_code == 401
    assert "expired" in res2.json()["detail"].lower()


def test_token_invalid(client, settings):
    headers = {"Authorization": "Bearer asda.asda.asda"}
    res = client.get(f"{settings.api_root}/events", headers=headers)
    assert res.status_code == 401
    assert "invalid" in res.json()["detail"].lower()
