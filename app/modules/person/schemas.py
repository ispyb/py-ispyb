"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

person_dict = {
    "personId": f_fields.Integer(required=True, description=""),
    "laboratoryId": f_fields.Integer(required=False, description=""),
    "siteId": f_fields.Integer(required=False, description=""),
    "personUUID": f_fields.String(required=False, description=""),
    "familyName": f_fields.String(required=False, description=""),
    "givenName": f_fields.String(required=False, description=""),
    "title": f_fields.String(required=False, description=""),
    "emailAddress": f_fields.String(required=False, description=""),
    "phoneNumber": f_fields.String(required=False, description=""),
    "login": f_fields.String(required=False, description=""),
    "faxNumber": f_fields.String(required=False, description=""),
    "recordTimeStamp": f_fields.DateTime(
        required=True, description="Creation or last update date/time"
    ),
    "externalId": f_fields.Integer(required=False, description=""),
    "cache": f_fields.String(required=False, description=""),
}


class PersonSchema(Schema):
    """Marshmallows schema class representing Person table"""

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
    externalId = ma_fields.Integer()
    cache = ma_fields.String()


f_person_schema = api.model("Person", person_dict)
ma_person_schema = PersonSchema()
