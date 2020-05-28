def test_proposal_route(flask_app, token):
    client = flask_app.test_client()
    api_root = flask_app.config["API_ROOT"]
    
    headers = {"Authorization": "Bearer " + token}
    response = client.get(api_root + "/proposals", headers=headers)
    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0, "No proposal returned"

    #proposal_id = response.json[0]['proposalId']
    #response = client.get(api_root + "/proposals/%d" % proposal_id, headers=headers)
    #assert response.status_code == 200, "Wrong status code"

    #response = client.get(api_root + "/proposals?page=1", headers=headers)
    #assert response.status_code == 200, "Wrong status code"
