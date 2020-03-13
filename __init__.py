from .database import db_proposals
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return Response("It works!"), 200

@app.route("/proposals/")
def proposals():
    all_proposals = db_proposals.get_all_proposals()
    return Response(str(all_proposals)), 200

if __name__ == "__main__":
    app.run(debug=True)

