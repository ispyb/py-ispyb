
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

image_quality_indicators_dict = {
        'imageQualityIndicatorsId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'imageId': f_fields.Integer(required=False, description=''),
        'autoProcProgramId': f_fields.Integer(required=True, description='Foreign key to the AutoProcProgram table'),
        'spotTotal': f_fields.Integer(required=False, description='Total number of spots'),
        'inResTotal': f_fields.Integer(required=False, description='Total number of spots in resolution range'),
        'goodBraggCandidates': f_fields.Integer(required=False, description='Total number of Bragg diffraction spots'),
        'iceRings': f_fields.Integer(required=False, description='Number of ice rings identified'),
        'method1Res': f_fields.Float(required=False, description='Resolution estimate 1 (see publication)'),
        'method2Res': f_fields.Float(required=False, description='Resolution estimate 2 (see publication)'),
        'maxUnitCell': f_fields.Float(required=False, description='Estimation of the largest possible unit cell edge'),
        'pctSaturationTop50Peaks': f_fields.Float(required=False, description='The fraction of the dynamic range being used'),
        'inResolutionOvrlSpots': f_fields.Integer(required=False, description='Number of spots overloaded'),
        'binPopCutOffMethod2Res': f_fields.Float(required=False, description='Cut off used in resolution limit calculation'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        'totalIntegratedSignal': f_fields.String(required=False, description=''),
        'dozor_score': f_fields.String(required=False, description='dozor_score'),
        'dataCollectionId': f_fields.Integer(required=False, description=''),
        'imageNumber': f_fields.Integer(required=False, description=''),
        }

class ImageQualityIndicatorsSchema(Schema):
    imageQualityIndicatorsId = ma_fields.Integer()
    imageId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    spotTotal = ma_fields.Integer()
    inResTotal = ma_fields.Integer()
    goodBraggCandidates = ma_fields.Integer()
    iceRings = ma_fields.Integer()
    method1Res = ma_fields.Float()
    method2Res = ma_fields.Float()
    maxUnitCell = ma_fields.Float()
    pctSaturationTop50Peaks = ma_fields.Float()
    inResolutionOvrlSpots = ma_fields.Integer()
    binPopCutOffMethod2Res = ma_fields.Float()
    recordTimeStamp = ma_fields.DateTime()
    totalIntegratedSignal = ma_fields.String()
    dozor_score = ma_fields.String()
    dataCollectionId = ma_fields.Integer()
    imageNumber = ma_fields.Integer()

f_image_quality_indicators_schema = api.model('ImageQualityIndicators', image_quality_indicators_dict)
ma_image_quality_indicators_schema = ImageQualityIndicatorsSchema()
