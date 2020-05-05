"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

auto_proc_integration_dict = {
    "autoProcIntegrationId": f_fields.Integer(
        required=True, description="Primary key (auto-incremented)"
    ),
    "dataCollectionId": f_fields.Integer(
        required=True, description="DataCollection item"
    ),
    "autoProcProgramId": f_fields.Integer(
        required=False, description="Related program item"
    ),
    "startImageNumber": f_fields.Integer(
        required=False, description="start image number"
    ),
    "endImageNumber": f_fields.Integer(required=False, description="end image number"),
    "refinedDetectorDistance": f_fields.Float(
        required=False, description="Refined DataCollection.detectorDistance"
    ),
    "refinedXBeam": f_fields.Float(
        required=False, description="Refined DataCollection.xBeam"
    ),
    "refinedYBeam": f_fields.Float(
        required=False, description="Refined DataCollection.yBeam"
    ),
    "rotationAxisX": f_fields.Float(required=False, description="Rotation axis"),
    "rotationAxisY": f_fields.Float(required=False, description="Rotation axis"),
    "rotationAxisZ": f_fields.Float(required=False, description="Rotation axis"),
    "beamVectorX": f_fields.Float(required=False, description="Beam vector"),
    "beamVectorY": f_fields.Float(required=False, description="Beam vector"),
    "beamVectorZ": f_fields.Float(required=False, description="Beam vector"),
    "cell_a": f_fields.Float(required=False, description="Unit cell"),
    "cell_b": f_fields.Float(required=False, description="Unit cell"),
    "cell_c": f_fields.Float(required=False, description="Unit cell"),
    "cell_alpha": f_fields.Float(required=False, description="Unit cell"),
    "cell_beta": f_fields.Float(required=False, description="Unit cell"),
    "cell_gamma": f_fields.Float(required=False, description="Unit cell"),
    "recordTimeStamp": f_fields.DateTime(
        required=False, description="Creation or last update date/time"
    ),
    "anomalous": f_fields.Integer(
        required=False, description="boolean type:0 noanoum - 1 anoum"
    ),
}


class AutoProcIntegrationSchema(Schema):
    """Marshmallows schema class representing AutoProcIntegration table"""

    autoProcIntegrationId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    startImageNumber = ma_fields.Integer()
    endImageNumber = ma_fields.Integer()
    refinedDetectorDistance = ma_fields.Float()
    refinedXBeam = ma_fields.Float()
    refinedYBeam = ma_fields.Float()
    rotationAxisX = ma_fields.Float()
    rotationAxisY = ma_fields.Float()
    rotationAxisZ = ma_fields.Float()
    beamVectorX = ma_fields.Float()
    beamVectorY = ma_fields.Float()
    beamVectorZ = ma_fields.Float()
    cell_a = ma_fields.Float()
    cell_b = ma_fields.Float()
    cell_c = ma_fields.Float()
    cell_alpha = ma_fields.Float()
    cell_beta = ma_fields.Float()
    cell_gamma = ma_fields.Float()
    recordTimeStamp = ma_fields.DateTime()
    anomalous = ma_fields.Integer()


f_auto_proc_integration_schema = api.model(
    "AutoProcIntegration", auto_proc_integration_dict
)
ma_auto_proc_integration_schema = AutoProcIntegrationSchema()
