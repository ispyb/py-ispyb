import abc
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from ispyb import app

class BaseAuth(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.token_list = [] 

    def generate_auth_token(self, username, expiration=600):
        roles = self.get_roles(username)
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': username})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user 

    @abc.abstractmethod
    def get_roles(self, user):
        result = []
        return result
