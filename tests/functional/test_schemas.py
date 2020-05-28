def test_schemas_route(flask_app, token):
    client = flask_app.test_client()
    api_root = flask_app.config["API_ROOT"]

    headers = {"Authorization": "Bearer " + token}
    response = client.get(api_root + "/schemas/available_names", headers=headers)
    assert response.status_code == 200, "Wrong status code"
    assert len(response.json) > 0, "No schemas returned"

    schema_name = response.json[0]
    response = client.get(api_root + "/schemas/%s" % schema_name, headers=headers)
    assert response.status_code == 200, "Wrong status code"
