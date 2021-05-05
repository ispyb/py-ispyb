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
        'ctfId': f_fields.Integer(required=True, description=''),
        'motionCorrectionId': f_fields.Integer(required=False, description=''),
        'autoProcProgramId': f_fields.Integer(required=False, description=''),
        'boxSizeX': f_fields.Float(required=False, description='Box size in x, Units: pixels'),
        'boxSizeY': f_fields.Float(required=False, description='Box size in y, Units: pixels'),
        'minResolution': f_fields.Float(required=False, description='Minimum resolution for CTF, Units: A'),
        'maxResolution': f_fields.Float(required=False, description='Units: A'),
        'minDefocus': f_fields.Float(required=False, description='Units: A'),
        'maxDefocus': f_fields.Float(required=False, description='Units: A'),
        'defocusStepSize': f_fields.Float(required=False, description='Units: A'),
        'astigmatism': f_fields.Float(required=False, description='Units: A'),
        'astigmatismAngle': f_fields.Float(required=False, description='Units: deg?'),
        'estimatedResolution': f_fields.Float(required=False, description='Units: A'),
        'estimatedDefocus': f_fields.Float(required=False, description='Units: A'),
        'amplitudeContrast': f_fields.Float(required=False, description='Units: %?'),
        'ccValue': f_fields.Float(required=False, description='Correlation value'),
        'fftTheoreticalFullPath': f_fields.String(required=False, description='Full path to the jpg image of the simulated FFT'),
        'comments': f_fields.String(required=False, description=''),
        }

class CTFSchema(Schema):
    """Marshmallows schema class representing CTF table"""

    ctfId = ma_fields.Integer()
    motionCorrectionId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    boxSizeX = ma_fields.Float()
    boxSizeY = ma_fields.Float()
    minResolution = ma_fields.Float()
    maxResolution = ma_fields.Float()
    minDefocus = ma_fields.Float()
    maxDefocus = ma_fields.Float()
    defocusStepSize = ma_fields.Float()
    astigmatism = ma_fields.Float()
    astigmatismAngle = ma_fields.Float()
    estimatedResolution = ma_fields.Float()
    estimatedDefocus = ma_fields.Float()
    amplitudeContrast = ma_fields.Float()
    ccValue = ma_fields.Float()
    fftTheoreticalFullPath = ma_fields.String()
    comments = ma_fields.String()

f_schema = api.model('CTF', dict_schema)
ma_schema = CTFSchema()
json_schema = JSONSchema().dump(ma_schema)
