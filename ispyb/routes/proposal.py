from flask_restplus import Resource

from ispyb import api
from ispyb.models import Proposal
from ispyb.schemas import ProposalSchema
from ispyb.auth import token_required

proposals_schema = ProposalSchema(many=True)


@api.route("/proposals")
class Proposals(Resource):
    """Proposals resource"""

    @api.doc(security="apikey")
    @token_required
    def get(self):
        """Returns all proposal"""
        proposals = Proposal.query.all()
        result = proposals_schema.dump(proposals)
        return {"data": result}
