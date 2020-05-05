"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

sample_dict = {
    "blSampleId": f_fields.Integer(required=True, description=""),
    "diffractionPlanId": f_fields.Integer(required=False, description=""),
    "crystalId": f_fields.Integer(required=False, description=""),
    "containerId": f_fields.Integer(required=False, description=""),
    "name": f_fields.String(required=False, description=""),
    "code": f_fields.String(required=False, description=""),
    "location": f_fields.String(required=False, description=""),
    "holderLength": f_fields.String(required=False, description=""),
    "loopLength": f_fields.String(required=False, description=""),
    "loopType": f_fields.String(required=False, description=""),
    "wireWidth": f_fields.String(required=False, description=""),
    "comments": f_fields.String(required=False, description=""),
    "completionStage": f_fields.String(required=False, description=""),
    "structureStage": f_fields.String(required=False, description=""),
    "publicationStage": f_fields.String(required=False, description=""),
    "publicationComments": f_fields.String(required=False, description=""),
    "blSampleStatus": f_fields.String(required=False, description=""),
    "isInSampleChanger": f_fields.Integer(required=False, description=""),
    "lastKnownCenteringPosition": f_fields.String(required=False, description=""),
    "recordTimeStamp": f_fields.DateTime(
        required=True, description="Creation or last update date/time"
    ),
    "SMILES": f_fields.String(
        required=False,
        description="the symbolic description of the structure of a chemical compound",
    ),
    "lastImageURL": f_fields.String(required=False, description=""),
    "positionId": f_fields.Integer(required=False, description=""),
    "blSubSampleId": f_fields.Integer(required=False, description=""),
    "screenComponentGroupId": f_fields.Integer(required=False, description=""),
    "volume": f_fields.Float(required=False, description=""),
    "dimension1": f_fields.String(required=False, description=""),
    "dimension2": f_fields.String(required=False, description=""),
    "dimension3": f_fields.String(required=False, description=""),
    "shape": f_fields.String(required=False, description=""),
    "subLocation": f_fields.Integer(
        required=False,
        description="Indicates the samples location on a multi-sample pin, where 1 is closest to the pin base",
    ),
    "packingfraction": f_fields.Float(required=False, description=""),
}


class SampleSchema(Schema):
    """Marshmallows schema class representing Sample table"""

    blSampleId = ma_fields.Integer()
    diffractionPlanId = ma_fields.Integer()
    crystalId = ma_fields.Integer()
    containerId = ma_fields.Integer()
    name = ma_fields.String()
    code = ma_fields.String()
    location = ma_fields.String()
    holderLength = ma_fields.String()
    loopLength = ma_fields.String()
    loopType = ma_fields.String()
    wireWidth = ma_fields.String()
    comments = ma_fields.String()
    completionStage = ma_fields.String()
    structureStage = ma_fields.String()
    publicationStage = ma_fields.String()
    publicationComments = ma_fields.String()
    blSampleStatus = ma_fields.String()
    isInSampleChanger = ma_fields.Integer()
    lastKnownCenteringPosition = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    SMILES = ma_fields.String()
    lastImageURL = ma_fields.String()
    positionId = ma_fields.Integer()
    blSubSampleId = ma_fields.Integer()
    screenComponentGroupId = ma_fields.Integer()
    volume = ma_fields.Float()
    dimension1 = ma_fields.String()
    dimension2 = ma_fields.String()
    dimension3 = ma_fields.String()
    shape = ma_fields.String()
    subLocation = ma_fields.Integer()
    packingfraction = ma_fields.Float()


f_sample_schema = api.model("Sample", sample_dict)
ma_sample_schema = SampleSchema()
