"""
ISPyB flask server
"""

import importlib
from functools import wraps
from flask import request, jsonify

import jwt

from ispyb import config, app

module_name = config["auth"]["module"]
class_name = config["auth"]["class"]
cls = getattr(importlib.import_module(module_name), class_name)

auth = cls()

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

        if config["general"]["master_token"] == token:
            app.logger.info("Master token validated")
            return f(*args, **kwargs)
        else:
            try:
                pyload = jwt.decode(token, app.config['SECRET_KEY'])
            except jwt.ExpiredSignatureError:
                return {"message": "Token expired. Please log in again"}, 401
            except jwt.InvalidTokenError:
                return {"message": "Invalid token. Please log in again"}, 401
            return f(*args, **kwargs)
    return decorated
