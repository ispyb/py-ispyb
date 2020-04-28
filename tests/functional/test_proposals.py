def test_get_all_proposals(client):
    response = client.get("/prop")

    assert response.status_code == 200
    print(response.json)
