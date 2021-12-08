from pyispyb.app.extensions import db


class Roles(db.Model):
    __tablename__ = 'Roles'

    rolesId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256))
    roles = db.Column(db.String(512))
