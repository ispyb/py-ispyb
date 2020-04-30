from functools import wraps

import jwt
from flask import current_app, request

from .auth_provider import AuthProvider

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

        print(111)
        print(token)
        if current_app.config.get("MASTER_TOKEN"):
            if current_app.config["MASTER_TOKEN"] == token:
                current_app.logger.info("Master token validated")
                return f(*args, **kwargs)
        try:
            pyload = jwt.decode(token, current_app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            current_app.logger.info("Token expired. Please log in again")
            print("Token expired. Please log in again")
            return {"message": "Token expired. Please log in again"}, 401
        except jwt.InvalidTokenError:
            print("Invalid token. Please log in again")
            return {"message": "Invalid token. Please log in again"}, 401
        return f(*args, **kwargs)
    return decorated
