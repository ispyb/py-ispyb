from flask import request, make_response
from flask_restx import Namespace, Resource

from app.extensions import auth_provider

api = Namespace('Login', description='Login namespace', path='/login')

@api.route("")
class Login(Resource):
    """Login resource"""

    def get(self):
        authorization = request.authorization

        if not authorization or not authorization.username or not authorization.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
        roles = auth_provider.get_roles(authorization.username, authorization.password)

        if not roles:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
        else:
            token = auth_provider.generate_token(authorization.username, roles) 
            return {'token': token,
                    'roles': roles
                    }
