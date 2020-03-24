import importlib
from functools import wraps
from flask import request

from ispyb import config

module_name = config['auth']['module']
class_name = config['auth']['class']
cls = getattr(importlib.import_module(module_name), class_name)

auth = cls()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message': 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message': 'Your token is wrong, wrong, wrong!!!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated