from flask import abort, jsonify, request
from flask_restplus import Resource

from ispyb import api, app
from ispyb.models.proposal import Proposal
from ispyb.schemas.proposal import ProposalSchema

proposal_schema = ProposalSchema()
proposals_schema = ProposalSchema(many=True)

"""
@api.route('/todos/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
"""

@api.route("/proposals")
class Proposals(Resource):

    def get(self):
        proposals = Proposal.query.all()
        result = proposals_schema.dump(proposals)
        return {'data': result}

