import sys
from requests import get, post

root_url = "http://localhost:5000/ispyb/api/v1"
response = get(root_url + "/auth/login", auth=(sys.argv[1], sys.argv[2]))
# Alternative get(root_url + "/auth/login", headers={'username': 'user',
# 'password': 'pass'}

if response.status_code == 200:
    roles = response.json()["roles"]
    token = response.json()["token"]
    print("Response: %s" % response.json())
    headers = {"Authorization": "Bearer " + token}

    print("-----------------------------------------")
    path = "/proposals"
    print("Request: %s%s" % (root_url, path))
    response = get(root_url + path, headers=headers)
    print("Status code: %d" % response.status_code)
    data = response.json()
    print(data)
    #proposal_id = data["rows"][0]["proposalId"]

    """
    proposal_id = 133
    path = "/proposals/%d" % proposal_id
    print("Request: %s%s" % (root_url, path))
    response = get(root_url + path, headers=headers)
    print("Status code: %d" % response.status_code)
    data = response.json()
    print('Data: %s' % str(data))
    """
else:
    print(response.reason, response.text)
