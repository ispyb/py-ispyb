def test_get_proposal_list(test_app):
    client = test_app.test_client()
    api_root = test_app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={"username": "user", "password": "pass"}
    )
    token = response.json["token"]

    assert token, "User not authetificated. No token returned"

    headers = {"Authorization": "Bearer " + token}
    response = client.get(api_root + "/prop/list", headers=headers)

    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0, "No proposal returned"
