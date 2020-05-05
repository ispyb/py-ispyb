from requests import get, post

root_url = "http://localhost:5000/ispyb/api/v1"

payload = {
        "username": "user",
        "password": "password"}
response = get(root_url + "/auth/login", json=payload)

print(response)


paths = ["/prop"]
for path in paths:
    print("-----------------------------------------")
    print("Request: %s%s" % (root_url, path))
    r = get(root_url + path)
    print("Status code: %d" % r.status_code)
    data = r.json()
    #for d in data:
    #    print(d)
    # print('Data: %s' % str(data))
