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
        'beamLineSetupId': f_fields.Integer(required=True, description=''),
        'detectorId': f_fields.Integer(required=False, description=''),
        'synchrotronMode': f_fields.String(required=False, description=''),
        'undulatorType1': f_fields.String(required=False, description=''),
        'undulatorType2': f_fields.String(required=False, description=''),
        'undulatorType3': f_fields.String(required=False, description=''),
        'focalSpotSizeAtSample': f_fields.Float(required=False, description=''),
        'focusingOptic': f_fields.String(required=False, description=''),
        'beamDivergenceHorizontal': f_fields.Float(required=False, description=''),
        'beamDivergenceVertical': f_fields.Float(required=False, description=''),
        'polarisation': f_fields.Float(required=False, description=''),
        'monochromatorType': f_fields.String(required=False, description=''),
        'setupDate': f_fields.DateTime(required=False, description=''),
        'synchrotronName': f_fields.String(required=False, description=''),
        'maxExpTimePerDataCollection': f_fields.String(required=False, description=''),
        'maxExposureTimePerImage': f_fields.Float(required=False, description='unit: seconds'),
        'minExposureTimePerImage': f_fields.String(required=False, description=''),
        'goniostatMaxOscillationSpeed': f_fields.String(required=False, description=''),
        'goniostatMaxOscillationWidth': f_fields.String(required=False, description='unit: degrees'),
        'goniostatMinOscillationWidth': f_fields.String(required=False, description=''),
        'maxTransmission': f_fields.String(required=False, description='unit: percentage'),
        'minTransmission': f_fields.String(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description='Creation or last update date/time'),
        'CS': f_fields.Float(required=False, description='Spherical Aberration, Units: mm?'),
        'beamlineName': f_fields.String(required=False, description='Beamline that this setup relates to'),
        'beamSizeXMin': f_fields.Float(required=False, description='unit: um'),
        'beamSizeXMax': f_fields.Float(required=False, description='unit: um'),
        'beamSizeYMin': f_fields.Float(required=False, description='unit: um'),
        'beamSizeYMax': f_fields.Float(required=False, description='unit: um'),
        'energyMin': f_fields.Float(required=False, description='unit: eV'),
        'energyMax': f_fields.Float(required=False, description='unit: eV'),
        'omegaMin': f_fields.Float(required=False, description='unit: degrees'),
        'omegaMax': f_fields.Float(required=False, description='unit: degrees'),
        'kappaMin': f_fields.Float(required=False, description='unit: degrees'),
        'kappaMax': f_fields.Float(required=False, description='unit: degrees'),
        'phiMin': f_fields.Float(required=False, description='unit: degrees'),
        'phiMax': f_fields.Float(required=False, description='unit: degrees'),
        'active': f_fields.Integer(required=True, description=''),
        'numberOfImagesMax': f_fields.Integer(required=False, description=''),
        'numberOfImagesMin': f_fields.Integer(required=False, description=''),
        'boxSizeXMin': f_fields.String(required=False, description='For gridscans, unit: um'),
        'boxSizeXMax': f_fields.String(required=False, description='For gridscans, unit: um'),
        'boxSizeYMin': f_fields.String(required=False, description='For gridscans, unit: um'),
        'boxSizeYMax': f_fields.String(required=False, description='For gridscans, unit: um'),
        'monoBandwidthMin': f_fields.String(required=False, description='unit: percentage'),
        'monoBandwidthMax': f_fields.String(required=False, description='unit: percentage'),
        }

class BeamLineSetupSchema(Schema):
    """Marshmallows schema class representing BeamLineSetup table"""

    beamLineSetupId = ma_fields.Integer()
    detectorId = ma_fields.Integer()
    synchrotronMode = ma_fields.String()
    undulatorType1 = ma_fields.String()
    undulatorType2 = ma_fields.String()
    undulatorType3 = ma_fields.String()
    focalSpotSizeAtSample = ma_fields.Float()
    focusingOptic = ma_fields.String()
    beamDivergenceHorizontal = ma_fields.Float()
    beamDivergenceVertical = ma_fields.Float()
    polarisation = ma_fields.Float()
    monochromatorType = ma_fields.String()
    setupDate = ma_fields.DateTime()
    synchrotronName = ma_fields.String()
    maxExpTimePerDataCollection = ma_fields.String()
    maxExposureTimePerImage = ma_fields.Float()
    minExposureTimePerImage = ma_fields.String()
    goniostatMaxOscillationSpeed = ma_fields.String()
    goniostatMaxOscillationWidth = ma_fields.String()
    goniostatMinOscillationWidth = ma_fields.String()
    maxTransmission = ma_fields.String()
    minTransmission = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    CS = ma_fields.Float()
    beamlineName = ma_fields.String()
    beamSizeXMin = ma_fields.Float()
    beamSizeXMax = ma_fields.Float()
    beamSizeYMin = ma_fields.Float()
    beamSizeYMax = ma_fields.Float()
    energyMin = ma_fields.Float()
    energyMax = ma_fields.Float()
    omegaMin = ma_fields.Float()
    omegaMax = ma_fields.Float()
    kappaMin = ma_fields.Float()
    kappaMax = ma_fields.Float()
    phiMin = ma_fields.Float()
    phiMax = ma_fields.Float()
    active = ma_fields.Integer()
    numberOfImagesMax = ma_fields.Integer()
    numberOfImagesMin = ma_fields.Integer()
    boxSizeXMin = ma_fields.String()
    boxSizeXMax = ma_fields.String()
    boxSizeYMin = ma_fields.String()
    boxSizeYMax = ma_fields.String()
    monoBandwidthMin = ma_fields.String()
    monoBandwidthMax = ma_fields.String()

f_schema = api.model('BeamLineSetup', dict_schema)
ma_schema = BeamLineSetupSchema()
json_schema = JSONSchema().dump(ma_schema)
