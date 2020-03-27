import importlib
import datetime
from functools import wraps

import jwt
from flask import request, jsonify

from ispyb import config, app

module_name = config["auth"]["module"]
class_name = config["auth"]["class"]
cls = getattr(importlib.import_module(module_name), class_name)

auth = cls()


TOKEN_EXP_TIME = 60 # in minutes

def generate_token(username):
    token = jwt.encode({
        'user': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXP_TIME)},
        app.config['SECRET_KEY'])
    return token.decode('UTF-8')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #Check if token is in header
        if "token" in request.headers:
            token = request.headers["token"]
        #Check if token is in args
        if not token:
            token = request.args.get('token')

        if not token:
            return {"message": "Token is missing."}, 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return {"message": "Invalid token"}, 401
        return f(*args, **kwargs)
    return decorated
