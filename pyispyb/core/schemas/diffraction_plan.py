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
        'diffractionPlanId': f_fields.Integer(required=True, description=''),
        'name': f_fields.String(required=False, description=''),
        'experimentKind': f_fields.String(required=False, description='enum(Default,MXPressE,MXPressO,MXPressE_SAD,MXScore,MXPressM,MAD,SAD,Fixed,Ligand binding,Refinement,OSC,MAD - Inverse Beam,SAD - Inverse Beam,MESH,XFE,Stepped transmission)'),
        'observedResolution': f_fields.Float(required=False, description=''),
        'minimalResolution': f_fields.Float(required=False, description=''),
        'exposureTime': f_fields.Float(required=False, description=''),
        'oscillationRange': f_fields.Float(required=False, description=''),
        'maximalResolution': f_fields.Float(required=False, description=''),
        'screeningResolution': f_fields.Float(required=False, description=''),
        'radiationSensitivity': f_fields.Float(required=False, description=''),
        'anomalousScatterer': f_fields.String(required=False, description=''),
        'preferredBeamSizeX': f_fields.Float(required=False, description=''),
        'preferredBeamSizeY': f_fields.Float(required=False, description=''),
        'preferredBeamDiameter': f_fields.Float(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'DIFFRACTIONPLANUUID': f_fields.String(required=False, description=''),
        'aimedCompleteness': f_fields.String(required=False, description=''),
        'aimedIOverSigmaAtHighestRes': f_fields.String(required=False, description=''),
        'aimedMultiplicity': f_fields.String(required=False, description=''),
        'aimedResolution': f_fields.String(required=False, description=''),
        'anomalousData': f_fields.Integer(required=False, description=''),
        'complexity': f_fields.String(required=False, description=''),
        'estimateRadiationDamage': f_fields.Integer(required=False, description=''),
        'forcedSpaceGroup': f_fields.String(required=False, description=''),
        'requiredCompleteness': f_fields.String(required=False, description=''),
        'requiredMultiplicity': f_fields.String(required=False, description=''),
        'requiredResolution': f_fields.String(required=False, description=''),
        'strategyOption': f_fields.String(required=False, description=''),
        'kappaStrategyOption': f_fields.String(required=False, description=''),
        'numberOfPositions': f_fields.Integer(required=False, description=''),
        'minDimAccrossSpindleAxis': f_fields.String(required=False, description='minimum dimension accross the spindle axis'),
        'maxDimAccrossSpindleAxis': f_fields.String(required=False, description='maximum dimension accross the spindle axis'),
        'radiationSensitivityBeta': f_fields.String(required=False, description=''),
        'radiationSensitivityGamma': f_fields.String(required=False, description=''),
        'minOscWidth': f_fields.Float(required=False, description=''),
        'recordTimeStamp': f_fields.DateTime(required=True, description='Creation or last update date/time'),
        'monochromator': f_fields.String(required=False, description='DMM or DCM'),
        'energy': f_fields.Float(required=False, description='eV'),
        'transmission': f_fields.Float(required=False, description='Decimal fraction in range [0,1]'),
        'boxSizeX': f_fields.Float(required=False, description='microns'),
        'boxSizeY': f_fields.Float(required=False, description='microns'),
        'kappaStart': f_fields.Float(required=False, description='degrees'),
        'axisStart': f_fields.Float(required=False, description='degrees'),
        'axisRange': f_fields.Float(required=False, description='degrees'),
        'numberOfImages': f_fields.Integer(required=False, description='The number of images requested'),
        'presetForProposalId': f_fields.Integer(required=False, description='Indicates this plan is available to all sessions on given proposal'),
        'beamLineName': f_fields.String(required=False, description='Indicates this plan is available to all sessions on given beamline'),
        'detectorId': f_fields.Integer(required=False, description=''),
        'distance': f_fields.String(required=False, description=''),
        'orientation': f_fields.String(required=False, description=''),
        'monoBandwidth': f_fields.String(required=False, description=''),
        'centringMethod': f_fields.String(required=False, description='enum(xray,loop,diffraction,optical)'),
        }

class DiffractionPlanSchema(Schema):
    """Marshmallows schema class representing DiffractionPlan table"""

    diffractionPlanId = ma_fields.Integer()
    name = ma_fields.String()
    experimentKind = ma_fields.String()
    observedResolution = ma_fields.Float()
    minimalResolution = ma_fields.Float()
    exposureTime = ma_fields.Float()
    oscillationRange = ma_fields.Float()
    maximalResolution = ma_fields.Float()
    screeningResolution = ma_fields.Float()
    radiationSensitivity = ma_fields.Float()
    anomalousScatterer = ma_fields.String()
    preferredBeamSizeX = ma_fields.Float()
    preferredBeamSizeY = ma_fields.Float()
    preferredBeamDiameter = ma_fields.Float()
    comments = ma_fields.String()
    DIFFRACTIONPLANUUID = ma_fields.String()
    aimedCompleteness = ma_fields.String()
    aimedIOverSigmaAtHighestRes = ma_fields.String()
    aimedMultiplicity = ma_fields.String()
    aimedResolution = ma_fields.String()
    anomalousData = ma_fields.Integer()
    complexity = ma_fields.String()
    estimateRadiationDamage = ma_fields.Integer()
    forcedSpaceGroup = ma_fields.String()
    requiredCompleteness = ma_fields.String()
    requiredMultiplicity = ma_fields.String()
    requiredResolution = ma_fields.String()
    strategyOption = ma_fields.String()
    kappaStrategyOption = ma_fields.String()
    numberOfPositions = ma_fields.Integer()
    minDimAccrossSpindleAxis = ma_fields.String()
    maxDimAccrossSpindleAxis = ma_fields.String()
    radiationSensitivityBeta = ma_fields.String()
    radiationSensitivityGamma = ma_fields.String()
    minOscWidth = ma_fields.Float()
    recordTimeStamp = ma_fields.DateTime()
    monochromator = ma_fields.String()
    energy = ma_fields.Float()
    transmission = ma_fields.Float()
    boxSizeX = ma_fields.Float()
    boxSizeY = ma_fields.Float()
    kappaStart = ma_fields.Float()
    axisStart = ma_fields.Float()
    axisRange = ma_fields.Float()
    numberOfImages = ma_fields.Integer()
    presetForProposalId = ma_fields.Integer()
    beamLineName = ma_fields.String()
    detectorId = ma_fields.Integer()
    distance = ma_fields.String()
    orientation = ma_fields.String()
    monoBandwidth = ma_fields.String()
    centringMethod = ma_fields.String()

f_schema = api.model('DiffractionPlan', dict_schema)
ma_schema = DiffractionPlanSchema()
json_schema = JSONSchema().dump(ma_schema)
