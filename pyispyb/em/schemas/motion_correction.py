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
        'motionCorrectionId': f_fields.Integer(required=True, description=''),
        'dataCollectionId': f_fields.Integer(required=False, description=''),
        'autoProcProgramId': f_fields.Integer(required=False, description=''),
        'imageNumber': f_fields.Integer(required=False, description='Movie number, sequential in time 1-n'),
        'firstFrame': f_fields.Integer(required=False, description='First frame of movie used'),
        'lastFrame': f_fields.Integer(required=False, description='Last frame of movie used'),
        'dosePerFrame': f_fields.Float(required=False, description='Dose per frame, Units: e-/A^2'),
        'doseWeight': f_fields.Float(required=False, description='Dose weight, Units: dimensionless'),
        'totalMotion': f_fields.Float(required=False, description='Total motion, Units: A'),
        'averageMotionPerFrame': f_fields.Float(required=False, description='Average motion per frame, Units: A'),
        'driftPlotFullPath': f_fields.String(required=False, description='Full path to the drift plot'),
        'micrographFullPath': f_fields.String(required=False, description='Full path to the micrograph'),
        'micrographSnapshotFullPath': f_fields.String(required=False, description='Full path to a snapshot (jpg) of the micrograph'),
        'patchesUsedX': f_fields.Integer(required=False, description='Number of patches used in x (for motioncor2)'),
        'patchesUsedY': f_fields.Integer(required=False, description='Number of patches used in y (for motioncor2)'),
        'fftFullPath': f_fields.String(required=False, description='Full path to the jpg image of the raw micrograph FFT'),
        'fftCorrectedFullPath': f_fields.String(required=False, description='Full path to the jpg image of the drift corrected micrograph FFT'),
        'comments': f_fields.String(required=False, description=''),
        'movieId': f_fields.Integer(required=False, description=''),
        }

class MotionCorrectionSchema(Schema):
    """Marshmallows schema class representing MotionCorrection table"""

    motionCorrectionId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    imageNumber = ma_fields.Integer()
    firstFrame = ma_fields.Integer()
    lastFrame = ma_fields.Integer()
    dosePerFrame = ma_fields.Float()
    doseWeight = ma_fields.Float()
    totalMotion = ma_fields.Float()
    averageMotionPerFrame = ma_fields.Float()
    driftPlotFullPath = ma_fields.String()
    micrographFullPath = ma_fields.String()
    micrographSnapshotFullPath = ma_fields.String()
    patchesUsedX = ma_fields.Integer()
    patchesUsedY = ma_fields.Integer()
    fftFullPath = ma_fields.String()
    fftCorrectedFullPath = ma_fields.String()
    comments = ma_fields.String()
    movieId = ma_fields.Integer()

f_schema = api.model('MotionCorrection', dict_schema)
ma_schema = MotionCorrectionSchema()
json_schema = JSONSchema().dump(ma_schema)
