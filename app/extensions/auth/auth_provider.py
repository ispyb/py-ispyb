"""
ISPyB flask server
"""

import abc
import jwt
import datetime
import importlib
from functools import wraps
from flask import current_app, request, jsonify


TOKEN_EXP_TIME = 2# in minutes
MASTER_TOKEN = None

class AuthProvider(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.tokens = {}
        self.site_auth = None

    def init_app(self, app):
        module_name = app.config["AUTH_MODULE"]
        class_name = app.config["AUTH_CLASS"]
        cls = getattr(importlib.import_module(module_name), class_name)
        self.site_auth = cls()

        assert app.config['SECRET_KEY'], "SECRET_KEY must be configured!"

        if app.config.get("MASTER_TOKEN"):
            global MASTER_TOKEN
            MASTER_TOKEN = app.config["MASTER_TOKEN"]

    def get_roles(self, user, password):
        return self.site_auth.get_roles(user, password)

    def generate_token(self, username, roles):
        token = jwt.encode({
            'sub': username,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXP_TIME)},
            current_app.config['SECRET_KEY'])
        return token.decode('UTF-8')
