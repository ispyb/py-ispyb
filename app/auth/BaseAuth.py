"""
ISPyB flask server
"""

import abc
import jwt
import datetime

from ispyb import app

TOKEN_EXP_TIME = 2# in minutes

class BaseAuth(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.tokens = {}

    @abc.abstractmethod
    def get_roles(self, user, password):
        result = []
        return result

    TOKEN_EXP_TIME = 60 # in minutes

    def generate_token(self, username, roles):
        token = jwt.encode({
            'sub': username,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXP_TIME)},
        app.config['SECRET_KEY'])
        return token.decode('UTF-8')
