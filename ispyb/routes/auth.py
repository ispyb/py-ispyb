import logging

from flask import abort, jsonify, request
from flask_restplus import Namespace, Resource

from ispyb import api, app
from ispyb.auth import auth

TOKEN_DURATION = 600

@api.route('/token')
class Token(Resource):
    def get(self):
        return {'hey': 'there'}