from flask import Response, jsonify

from ispyb import server
from ispyb.database import db_proposals


@server.route("/ispyb/api/proposals/", methods=["GET"])
def get_all_proposals():
    return Response(str(db_proposals.get_all_proposals())), 200
    #resp = jsonify({"proposals": db_proposals.get_all_proposals()})
    #resp.status_code = 200
    #return resp
