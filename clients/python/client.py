from requests import get, post

root_url = "http://localhost:5000/ispyb/api/v1"

username = "user"
response = get(root_url + "/auth/login", auth=(username, "pass"))
# Alternative get(root_url + "/auth/login", headers={'username': 'user',
# 'password': 'pass'}

if response.status_code == 200:
    roles = response.json()["roles"]
    token = response.json()["token"]
    print("User %s validated" % username)
    print("Token: %s" % token)
    paths = ["/proposals"]
    headers = {"Authorization": "Bearer " + token}
    for path in paths:
        print("-----------------------------------------")
        print("Request: %s%s" % (root_url, path))
        response = get(root_url + path, headers=headers)
        print("Status code: %d" % response.status_code)
        data = response.json()
        print(len(data))
    headers = {"Authorization": "invalid token"}
    for path in paths:
        print("-----------------------------------------")
        print("Request: %s%s" % (root_url, path))
        response = get(root_url + path, headers=headers)
        print("Status code: %d" % response.status_code)
        print("Response text: %s" % response.reason)
else:
    print("Unable to validate user %s" % username)
    print(response.reason, response.text)
