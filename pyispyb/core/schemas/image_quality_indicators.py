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
        'dataCollectionId': f_fields.Integer(required=True, description=''),
        'imageNumber': f_fields.Integer(required=True, description=''),
        'imageId': f_fields.Integer(required=False, description=''),
        'autoProcProgramId': f_fields.Integer(required=False, description='Foreign key to the AutoProcProgram table'),
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
        'driftFactor': f_fields.Float(required=False, description='EM movie drift factor'),
        }

class ImageQualityIndicatorsSchema(Schema):
    """Marshmallows schema class representing ImageQualityIndicators table"""

    dataCollectionId = ma_fields.Integer()
    imageNumber = ma_fields.Integer()
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
    driftFactor = ma_fields.Float()

f_schema = api.model('ImageQualityIndicators', dict_schema)
ma_schema = ImageQualityIndicatorsSchema()
json_schema = JSONSchema().dump(ma_schema)
