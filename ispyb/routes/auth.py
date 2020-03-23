import logging

from flask import abort, jsonify, request

from ispyb import server
from ispyb.auth import auth

TOKEN_DURATION = 600

@server.route("/ispyb/api/token", methods=["GET"])
def get_token():
    logging.getLogger('ispyb.routes').debug('Getting token')
    token = auth.generate_auth_token(TOKEN_DURATION)
    return jsonify({'token': token.decode('ascii'), 'duration': TOKEN_DURATION}) 
