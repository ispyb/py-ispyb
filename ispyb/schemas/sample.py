
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

sample_dict = {
        'blSampleId': f_fields.Integer(),
        'diffractionPlanId': f_fields.Integer(),
        'crystalId': f_fields.Integer(),
        'containerId': f_fields.Integer(),
        'name': f_fields.String(),
        'code': f_fields.String(),
        'location': f_fields.String(),
        'holderLength': f_fields.String(),
        'loopLength': f_fields.String(),
        'loopType': f_fields.String(),
        'wireWidth': f_fields.String(),
        'comments': f_fields.String(),
        'completionStage': f_fields.String(),
        'structureStage': f_fields.String(),
        'publicationStage': f_fields.String(),
        'publicationComments': f_fields.String(),
        'blSampleStatus': f_fields.String(),
        'isInSampleChanger': f_fields.String(),
        'lastKnownCenteringPosition': f_fields.String(),
        'POSITIONID': f_fields.Integer(),
        'recordTimeStamp': f_fields.DateTime(),
        'SMILES': f_fields.String(),
        'blSubSampleId': f_fields.Integer(),
        'lastImageURL': f_fields.String(),
        'screenComponentGroupId': f_fields.Integer(),
        'volume': f_fields.Integer(),
        'dimension1': f_fields.Integer(),
        'dimension2': f_fields.Integer(),
        'dimension3': f_fields.Integer(),
        'shape': f_fields.String(),
        'packingFraction': f_fields.String(),
        'preparationTemeprature': f_fields.String(),
        'preparationHumidity': f_fields.String(),
        'blottingTime': f_fields.Integer(),
        'blottingForce': f_fields.Integer(),
        'blottingDrainTime': f_fields.Integer(),
        'support': f_fields.String(),
        'subLocation': f_fields.String(),
        }

class SampleSchema(Schema):
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
    isInSampleChanger = ma_fields.String()
    lastKnownCenteringPosition = ma_fields.String()
    POSITIONID = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()
    SMILES = ma_fields.String()
    blSubSampleId = ma_fields.Integer()
    lastImageURL = ma_fields.String()
    screenComponentGroupId = ma_fields.Integer()
    volume = ma_fields.Integer()
    dimension1 = ma_fields.Integer()
    dimension2 = ma_fields.Integer()
    dimension3 = ma_fields.Integer()
    shape = ma_fields.String()
    packingFraction = ma_fields.String()
    preparationTemeprature = ma_fields.String()
    preparationHumidity = ma_fields.String()
    blottingTime = ma_fields.Integer()
    blottingForce = ma_fields.Integer()
    blottingDrainTime = ma_fields.Integer()
    support = ma_fields.String()
    subLocation = ma_fields.String()
