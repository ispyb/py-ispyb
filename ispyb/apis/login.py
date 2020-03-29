print(9)
from flask import request
from flask_restplus import Namespace, Resource
print(1)
from ispyb import app, auth
print(2)
ns = Namespace('Login', description='Login namespace', path='login')

@ns.route("/")
class Login(Resource):
    """Crystal list resource"""

    def get(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    roles = auth.get_roles(auth.username, auth.password)

    if not roles:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    else:
        token = auth.generate_token(auth.username, roles) 
        return token
