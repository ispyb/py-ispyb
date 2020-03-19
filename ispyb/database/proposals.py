from ispyb import db, config


class Proposals(db.Model):
    __tablename__ = config["db_table_map"]["proposal"]
    proposalId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)

    def get_all_proposals(self):
        all_proposals = self.query.all()
        result = []
        for proposal in all_proposals:
            result.append(self.convert_to_dict(proposal))
        return result

    def convert_to_dict(self, proposal):
        result ={'id': proposal.proposalId,
                 'title': proposal.title}
        return result

    def get_proposal_by_id(self, proposal_id):
        proposal = self.query.filter_by(proposalId=proposal_id).first()
        return self.convert_to_dict(proposal)
