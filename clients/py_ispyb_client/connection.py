from requests import get, post

AUTH_PATH = "/auth/login"

class Connection():

    def __init__(self, root_url, username, password):
        self.connected = False
        self.root_url = root_url
        self.roles = []
        self.token = None
        
        response = get(root_url + AUTH_PATH, auth=(username, password))

        if response.status_code == 200:
            self.connected = True
            roles = response.json()["roles"]
            token = response.json()["token"]
