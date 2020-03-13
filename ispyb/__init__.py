import os
import sys

from flask import Flask, Response

server = Flask(__name__)

fname = os.path.dirname(__file__)
sys.path.insert(0, fname)

from ispyb.routes import (proposal)

@server.route("/")
def index():
    return Response("It works!"), 200

"""
@server.route("/proposals/")
def proposals():
    all_proposals = db_proposals.get_all_proposals()
    return Response(str(all_proposals)), 200
"""

if __name__ == "__main__":
    server.run(debug=True)
