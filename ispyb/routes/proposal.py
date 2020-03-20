import logging

from flask import abort, jsonify, request

from ispyb import server, auth
from ispyb.database import db_proposals


@server.route("/ispyb/api/<token>/proposal/list", methods=["GET"])
def get_all_proposals(token):
    logging.getLogger('ispyb.routes').debug('Getting all proposals...')
    token = request.json.get('token')
    if auth.verify_auth_token(token):
        return jsonify({'data': db_proposals.get_all_proposals()})
    else:
        logging.getLogger('ispyb.routes').error('No proposals returned. Invalid token')
        abort(400)

@server.route("/ispyb/api/<token>/proposal/<proposalId>/get", methods=["GET"])
def get_proposal_by_id(token, proposalId):
    token = request.json.get('token')    
    proposals_id = request.json.get('proposalId')
    return jsonify({'data': db_proposals.get_proposal_by_id(proposal_id)})
