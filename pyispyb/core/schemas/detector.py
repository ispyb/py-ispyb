"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"



from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

dict_schema = {
        'detectorId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'detectorType': f_fields.String(required=False, description=''),
        'detectorManufacturer': f_fields.String(required=False, description=''),
        'detectorModel': f_fields.String(required=False, description=''),
        'detectorPixelSizeHorizontal': f_fields.Float(required=False, description=''),
        'detectorPixelSizeVertical': f_fields.Float(required=False, description=''),
        'DETECTORMAXRESOLUTION': f_fields.Float(required=False, description=''),
        'DETECTORMINRESOLUTION': f_fields.Float(required=False, description=''),
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
        'density': f_fields.Float(required=False, description=''),
        'composition': f_fields.String(required=False, description=''),
        'numberOfPixelsX': f_fields.Integer(required=False, description='Detector number of pixels in x'),
        'numberOfPixelsY': f_fields.Integer(required=False, description='Detector number of pixels in y'),
        'detectorRollMin': f_fields.String(required=False, description='unit: degrees'),
        'detectorRollMax': f_fields.String(required=False, description='unit: degrees'),
        'localName': f_fields.String(required=False, description='Colloquial name for the detector'),
        }

class DetectorSchema(Schema):
    """Marshmallows schema class representing Detector table"""

    detectorId = ma_fields.Integer()
    detectorType = ma_fields.String()
    detectorManufacturer = ma_fields.String()
    detectorModel = ma_fields.String()
    detectorPixelSizeHorizontal = ma_fields.Float()
    detectorPixelSizeVertical = ma_fields.Float()
    DETECTORMAXRESOLUTION = ma_fields.Float()
    DETECTORMINRESOLUTION = ma_fields.Float()
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
    density = ma_fields.Float()
    composition = ma_fields.String()
    numberOfPixelsX = ma_fields.Integer()
    numberOfPixelsY = ma_fields.Integer()
    detectorRollMin = ma_fields.String()
    detectorRollMax = ma_fields.String()
    localName = ma_fields.String()

f_schema = api.model('Detector', dict_schema)
ma_schema = DetectorSchema()
json_schema = JSONSchema().dump(ma_schema)
