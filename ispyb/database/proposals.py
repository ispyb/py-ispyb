from ispyb import db, config
from .schema import Proposal
from sqlalchemy import inspect


class Proposals(db.Model, Proposal):
    def get_all_proposals(self):
        all_proposals = self.query.all()
        result = []
        for proposal in all_proposals:
            result.append(self.object_as_dict(proposal))
        return result

    def object_as_dict(self, obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def get_proposal_by_id(self, proposal_id):
        proposal = self.query.filter_by(proposalId=proposal_id).first()
        return self.object_as_dict(proposal)
