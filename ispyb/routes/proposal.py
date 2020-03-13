from flask import Response, jsonify

from ispyb import server
from ispyb.database import db_proposals


@server.route("/ispyb/api/proposal/list", methods=["GET"])
def get_all_proposals():
    return Response(str(db_proposals.get_all_proposals())), 200
    #resp = jsonify({"proposals": db_proposals.get_all_proposals()})
    #resp.status_code = 200
    #return resp

@server.route("/ispyb/api/proposal/get/<code>", methods=["GET"])
def get_proposal_by_code_number(code):
    return Response("Not found"), 200
