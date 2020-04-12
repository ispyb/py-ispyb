
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

person_dict = {
        'personId': f_fields.Integer(),
        'laboratoryId': f_fields.Integer(),
        'siteId': f_fields.Integer(),
        'personUUID': f_fields.String(),
        'familyName': f_fields.String(),
        'givenName': f_fields.String(),
        'title': f_fields.String(),
        'emailAddress': f_fields.String(),
        'phoneNumber': f_fields.String(),
        'login': f_fields.String(),
        'faxNumber': f_fields.String(),
        'recordTimeStamp': f_fields.DateTime(),
        'cache': f_fields.String(),
        'externalId': f_fields.Integer(),
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
