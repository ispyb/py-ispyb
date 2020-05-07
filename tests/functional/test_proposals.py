def test_get_proposal_list(test_app):
    client = test_app.test_client()

    response = client.get(
            "/ispyb/api/v1/auth/login",
            headers={'username':'user', 'password': 'pass'})
    token = response.json['token']

    assert token, 'User not authetificated. No token returned'

    headers = {'token': token}
    response = client.get("/ispyb/api/v1/prop", headers=headers)


    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0 , "No proposal returned"
