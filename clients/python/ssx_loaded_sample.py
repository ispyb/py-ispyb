import os
import sys
import json
from requests import get, post

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)

from tests.ssx.data import sample_delivery_device_list

root_url = "http://localhost:5010/ispyb/api/v1/ssx"
response = get(root_url + "/auth/login", auth=("admin", "pass"))
token = response.json()["token"]
# Alternative get(root_url + "/auth/login", headers={'username': 'user',
# 'password': 'pass'}

headers = {
    "Authorization": "Bearer " + str(token),
    "Content-Type":  "application/json"
    }
path = root_url + "/samples/delivery_devices"


response = post(path, json=sample_delivery_device_list[0], headers=headers)

print(response.status_code)
print(response.text)
