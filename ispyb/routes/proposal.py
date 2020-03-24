from flask import abort, jsonify, request

from ispyb import app
from ispyb.models.proposal import ProposalModel
from ispyb.schemas.proposal import ProposalSchema

proposal_schema = ProposalSchema()
proposals_schema = ProposalSchema(many=True)

@app.route("/proposals/")
def proposals():
    all_proposals = ProposalModel.all()
    return proposal_schema.dump(all_users)


@app.route("/proposals/<id>")
def proposal_detail(id):
    proposal = ProposalModel.get(id)
    return proposal_schema.dump(proposal)

