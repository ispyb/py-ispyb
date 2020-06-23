import os
import sys
import json
from requests import get, post

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)


from tests.data import test_proposal

root_url = "http://localhost:5000/ispyb/api/v1"
response = get(root_url + "/auth/login", auth=("admin", "pass"))
token = response.json()["token"]
# Alternative get(root_url + "/auth/login", headers={'username': 'user',
# 'password': 'pass'}

"""
if response.status_code == 200:
    roles = response.json()["roles"]
    token = response.json()["token"]
    print("User %s validated" % username)
    print("Token: %s" % token)
    headers = {"Authorization": "Bearer " + token}
    
    
    print("-----------------------------------------")

    path = "/schemas/proposal"
    
    response = get(root_url + path, headers=headers)
    print("Status code: %d" % response.status_code)
    data = response.json()
    for prop in (data['definitions']['ProposalSchema']['properties']):
        print(prop)

          
else:
    print("Unable to validate user %s" % username)
    print(response.reason, response.text)
"""
headers = {"Authorization": "Bearer " + str(token)}
path = root_url + "/proposals"
print(test_proposal)
response = post(path, json=test_proposal, headers=headers)

print(response.status_code)
