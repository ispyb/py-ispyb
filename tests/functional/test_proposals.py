def test_proposal_route(test_app):
    client = test_app.test_client()
    api_root = test_app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={"username": "user", "password": "pass"}
    )
    token = response.json["token"]
    assert token, "User not authenticated. No token returned"

    headers = {"Authorization": "Bearer " + token}
    response = client.get(api_root + "/proposals", headers=headers)
    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0, "No proposal returned"

    response = client.get(api_root + "/proposals/1", headers=headers)
    assert response.status_code == 200, "Wrong status code"

    
    response = client.get(api_root + "/proposals/page/1", headers=headers)
    assert response.status_code == 200, "Wrong status code"
