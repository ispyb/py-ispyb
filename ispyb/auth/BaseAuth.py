import abc

from ispyb import server

class BaseAuth(object):

    __metaclass__ = abc.ABCMeta

    def generate_auth_token(self, expiration=600):
        s = Serializer(server.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(server.config['SECRET_KEY'])
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
