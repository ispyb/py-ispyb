from ispyb import db

class Proposal(db.Model):
    __tablename__ = 'Proposal'
    proposalId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    proposalCode = db.Column(db.String(45))
    proposalNumber = db.Column(db.String(45))

    def __repr__(self):
        return 'Proposal {}'.format(self.title)
