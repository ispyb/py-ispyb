from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields

person_dict = {
    'personId': fields.Integer(),
    'laboratoryId': fields.Integer(),
    'siteId': fields.Integer(),
    'personUUID': fields.String(),
    'familyName': fields.String(),
    'givenName': fields.String(),
    'title': fields.String(),
    'emailAddress': fields.String(),
    'phoneNumber': fields.String(),
    'login': fields.String(),
    'faxNumber': fields.String(),
    'recordTimeStamp': fields.DateTime(),
    'cache': fields.String(),
    'externalId': fields.Integer(),
    'Laboratory': fields.Integer(),
    'Project': fields.Integer(),
    'UserGroup': fields.Integer()
        }

class PersonSchema(Schema):
    personId = ma_fields.Integer()
    laboratoryId = ma_fields.Integer()
    siteId = ma_fields.Integer()
    personUUID = ma_fields.String()
    familyName = ma_fields.String()
    givenName = ma_fields.String()
    title = ma_fields.String()
    emailAddress = ma_fields.String()
    phoneNumber = ma_fields.String()
    login = ma_fields.String()
    faxNumber = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    cache = ma_fields.String()
    externalId = ma_fields.Integer()
    Laboratory = ma_fields.Integer()
    Project = ma_fields.Integer()
    UserGroup = ma_fields.Integer()
