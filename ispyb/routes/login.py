from flask import request, make_response
from flask_restplus import Resource

from ispyb import api, app
from ispyb import auth


@api.route("/login")
class Login(Resource):
    def get(self):
        auth = request.authorization
        if not auth:
            app.logger.info('No authorization found in request')
            return make_response(
                    'Could not verify the user. No authorization info available',
                    401,
                    {'WWW-Authenticate': 'Basic realm="Login required"'})
        else:
            if auth.password == 'mxpass':

                """
                token = jwt.encode({
                    'user': auth.username,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                    app.config['SECRET_KEY'])
                return token.decode('UTF-8')
                """
            else:
                return make_response('Could not verify the user. Password is incorect', 401)
