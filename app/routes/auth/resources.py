from flask import request, make_response
from flask_restx import Namespace, Resource

from app.extensions import auth_provider

api = Namespace(
    "Authentification", description="authentification namespace", path="/auth"
)


@api.route("/login")
class Login(Resource):
    """Login resource"""

    def get(self):
        authorization = request.authorization
 
        if (
            not authorization
            or not authorization.username
            or not authorization.password
        ):
            if not request.headers.get('username') or not request.headers.get('password'): 
                return make_response(
                        "Could not verify",
                        401,
                        {"WWW-Authenticate": 'Basic realm="Login required!"'},
            )
            else:
                username = request.headers.get('username')
                password = request.headers.get('password')
        else:
            username = authorization.username
            password = authorization.password

        roles = auth_provider.get_roles(username, password)
        if not roles:
            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm="Login required!"'},
            )
        else:
            token = auth_provider.generate_token(username, roles)
            return {"token": token, "roles": roles}
