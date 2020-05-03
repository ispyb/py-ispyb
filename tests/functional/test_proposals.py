def test_get_proposal_list(test_app):
    client = test_app.test_client()
    response = client.get("/ispyb/api/v1/prop")
    
    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0 , "No proposal returned"
