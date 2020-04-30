"""
ISPyB flask server
"""

class DummyAuth(object):
    def get_roles(self, username, password):
        result = []
        if username.startswith("user"):
            result.append("user")
        if username.startswith("manager"):
            results.append("manager")
        return result
