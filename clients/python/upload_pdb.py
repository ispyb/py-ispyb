import sys
from requests import get, post, patch

root_url = "http://localhost:5000/ispyb/api/v1"
token = "MasterToken"
headers = {"Authorization": "Bearer " + token}
crystal_id = 1

print("-----------------------------------------")
path = "/samples/crystals/%d/pdb?pdbFileName=7MH1.pdb" % crystal_id
print("[GET]: %s%s" % (root_url, path))
response = get(root_url + path, headers=headers)
print("Status code: %d" % response.status_code)
print(response.json())

"""
path="/samples/crystals/%d/pdb" % crystal_id
filepath="/home/mxuser/Downloads/7dvf.pdb"
files = {"file": open(filepath, "rb")}
print("[PATCH]: %s%s" % (root_url, path))
response = patch(root_url + path, headers=headers, files=files)
print("Status code: %d" % response.status_code)
print(response.json())
"""
