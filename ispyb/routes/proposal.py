from flask import jsonify, request

from ispyb import server
from ispyb.database import db_proposals


@server.route("/ispyb/api/proposal/list", methods=["GET"])
def get_all_proposals():
    return jsonify({'data': db_proposals.get_all_proposals()})

@server.route("/ispyb/api/proposal/<proposalId>/get", methods=["GET"])
def get_proposal_by_id(proposalId):
    return jsonify({'data': db_proposals.get_proposal_by_id(proposalId)})
