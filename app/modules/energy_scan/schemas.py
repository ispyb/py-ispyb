"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

energy_scan_dict = {
    "energyScanId": f_fields.Integer(required=True, description=""),
    "sessionId": f_fields.Integer(required=True, description=""),
    "blSampleId": f_fields.Integer(required=False, description=""),
    "fluorescenceDetector": f_fields.String(required=False, description=""),
    "scanFileFullPath": f_fields.String(required=False, description=""),
    "choochFileFullPath": f_fields.String(required=False, description=""),
    "jpegChoochFileFullPath": f_fields.String(required=False, description=""),
    "element": f_fields.String(required=False, description=""),
    "startEnergy": f_fields.Float(required=False, description=""),
    "endEnergy": f_fields.Float(required=False, description=""),
    "transmissionFactor": f_fields.Float(required=False, description=""),
    "exposureTime": f_fields.Float(required=False, description=""),
    "axisPosition": f_fields.Float(required=False, description=""),
    "synchrotronCurrent": f_fields.Float(required=False, description=""),
    "temperature": f_fields.Float(required=False, description=""),
    "peakEnergy": f_fields.Float(required=False, description=""),
    "peakFPrime": f_fields.Float(required=False, description=""),
    "peakFDoublePrime": f_fields.Float(required=False, description=""),
    "inflectionEnergy": f_fields.Float(required=False, description=""),
    "inflectionFPrime": f_fields.Float(required=False, description=""),
    "inflectionFDoublePrime": f_fields.Float(required=False, description=""),
    "xrayDose": f_fields.Float(required=False, description=""),
    "startTime": f_fields.DateTime(required=False, description=""),
    "endTime": f_fields.DateTime(required=False, description=""),
    "edgeEnergy": f_fields.String(required=False, description=""),
    "filename": f_fields.String(required=False, description=""),
    "beamSizeVertical": f_fields.Float(required=False, description=""),
    "beamSizeHorizontal": f_fields.Float(required=False, description=""),
    "crystalClass": f_fields.String(required=False, description=""),
    "comments": f_fields.String(required=False, description=""),
    "flux": f_fields.String(
        required=False, description="flux measured before the energyScan"
    ),
    "flux_end": f_fields.String(
        required=False, description="flux measured after the energyScan"
    ),
    "workingDirectory": f_fields.String(required=False, description=""),
    "blSubSampleId": f_fields.Integer(required=False, description=""),
}


class EnergyScanSchema(Schema):
    """Marshmallows schema class representing EnergyScan table"""

    energyScanId = ma_fields.Integer()
    sessionId = ma_fields.Integer()
    blSampleId = ma_fields.Integer()
    fluorescenceDetector = ma_fields.String()
    scanFileFullPath = ma_fields.String()
    choochFileFullPath = ma_fields.String()
    jpegChoochFileFullPath = ma_fields.String()
    element = ma_fields.String()
    startEnergy = ma_fields.Float()
    endEnergy = ma_fields.Float()
    transmissionFactor = ma_fields.Float()
    exposureTime = ma_fields.Float()
    axisPosition = ma_fields.Float()
    synchrotronCurrent = ma_fields.Float()
    temperature = ma_fields.Float()
    peakEnergy = ma_fields.Float()
    peakFPrime = ma_fields.Float()
    peakFDoublePrime = ma_fields.Float()
    inflectionEnergy = ma_fields.Float()
    inflectionFPrime = ma_fields.Float()
    inflectionFDoublePrime = ma_fields.Float()
    xrayDose = ma_fields.Float()
    startTime = ma_fields.DateTime()
    endTime = ma_fields.DateTime()
    edgeEnergy = ma_fields.String()
    filename = ma_fields.String()
    beamSizeVertical = ma_fields.Float()
    beamSizeHorizontal = ma_fields.Float()
    crystalClass = ma_fields.String()
    comments = ma_fields.String()
    flux = ma_fields.String()
    flux_end = ma_fields.String()
    workingDirectory = ma_fields.String()
    blSubSampleId = ma_fields.Integer()


f_energy_scan_schema = api.model("EnergyScan", energy_scan_dict)
ma_energy_scan_schema = EnergyScanSchema()
