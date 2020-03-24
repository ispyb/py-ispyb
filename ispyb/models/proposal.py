from ispyb import db

class ProposalModel(db.Model):

    proposalId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    proposalCode = db.Column(db.String(45))
    proposalNumber = db.Column(db.String(45))

