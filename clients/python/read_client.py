import sys
from requests import get, post

root_url = "http://localhost:5000/ispyb/api/v1"
proposal_id = sys.argv[1]
if len(sys.argv) > 2:
    token = sys.argv[2]
else:
    response = get(root_url + "/auth/login", auth=("mxuser", "mxpass"))
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
for prop in data["data"]["rows"]:
    print(prop)


print("-----------------------------------------")
path = "/sessions"
print("Request: %s%s" % (root_url, path))
headers["proposal_id"] = proposal_id
response = get(root_url + path, headers=headers)
print("Status code: %d" % response.status_code)
if response.status_code == 200:
    data = response.json()
    for prop in data["data"]["rows"]:
        print(prop)
else:
    print(response.text)

