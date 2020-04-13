
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

detector_dict = {
        'detectorId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'detectorType': f_fields.String(required=False, description=''),
        'detectorManufacturer': f_fields.String(required=False, description=''),
        'detectorModel': f_fields.String(required=False, description=''),
        'detectorPixelSizeHorizontal': f_fields.Float(required=False, description=''),
        'detectorPixelSizeVertical': f_fields.Float(required=False, description=''),
        'detectorSerialNumber': f_fields.String(required=False, description=''),
        'detectorDistanceMin': f_fields.String(required=False, description=''),
        'detectorDistanceMax': f_fields.String(required=False, description=''),
        'trustedPixelValueRangeLower': f_fields.String(required=False, description=''),
        'trustedPixelValueRangeUpper': f_fields.String(required=False, description=''),
        'sensorThickness': f_fields.Float(required=False, description=''),
        'overload': f_fields.Float(required=False, description=''),
        'XGeoCorr': f_fields.String(required=False, description=''),
        'YGeoCorr': f_fields.String(required=False, description=''),
        'detectorMode': f_fields.String(required=False, description=''),
        'detectorMaxResolution': f_fields.Float(required=False, description=''),
        'detectorMinResolution': f_fields.Float(required=False, description=''),
        'CS': f_fields.Float(required=False, description='Unit: mm'),
        'density': f_fields.Float(required=False, description=''),
        'composition': f_fields.String(required=False, description=''),
        'numberOfPixelsX': f_fields.Integer(required=False, description=''),
        'numberOfPixelsY': f_fields.Integer(required=False, description=''),
        'localName': f_fields.String(required=False, description='Colloquial name for the detector'),
        }

class DetectorSchema(Schema):
    detectorId = ma_fields.Integer()
    detectorType = ma_fields.String()
    detectorManufacturer = ma_fields.String()
    detectorModel = ma_fields.String()
    detectorPixelSizeHorizontal = ma_fields.Float()
    detectorPixelSizeVertical = ma_fields.Float()
    detectorSerialNumber = ma_fields.String()
    detectorDistanceMin = ma_fields.String()
    detectorDistanceMax = ma_fields.String()
    trustedPixelValueRangeLower = ma_fields.String()
    trustedPixelValueRangeUpper = ma_fields.String()
    sensorThickness = ma_fields.Float()
    overload = ma_fields.Float()
    XGeoCorr = ma_fields.String()
    YGeoCorr = ma_fields.String()
    detectorMode = ma_fields.String()
    detectorMaxResolution = ma_fields.Float()
    detectorMinResolution = ma_fields.Float()
    CS = ma_fields.Float()
    density = ma_fields.Float()
    composition = ma_fields.String()
    numberOfPixelsX = ma_fields.Integer()
    numberOfPixelsY = ma_fields.Integer()
    localName = ma_fields.String()
