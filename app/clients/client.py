import requests

root_url = "http://localhost:8000/ispyb/api/v1"
paths = ["/prop"]
for path in paths:
    print("-----------------------------------------")
    print("Request: %s%s" % (root_url, path))
    r = requests.get(root_url + path)
    print("Status code: %d" % r.status_code)
    data = r.json()
    for d in data:
        print(d)
    # print('Data: %s' % str(data))
