"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

auto_proc_scaling_dict = {
    "autoProcScalingId": f_fields.Integer(
        required=True, description="Primary key (auto-incremented)"
    ),
    "autoProcId": f_fields.Integer(
        required=False, description="Related autoProc item (used by foreign key)"
    ),
    "recordTimeStamp": f_fields.DateTime(
        required=False, description="Creation or last update date/time"
    ),
    "resolutionEllipsoidAxis11": f_fields.Float(
        required=False, description="Eigenvector for first diffraction limit, coord 1"
    ),
    "resolutionEllipsoidAxis12": f_fields.Float(
        required=False, description="Eigenvector for first diffraction limit, coord 2"
    ),
    "resolutionEllipsoidAxis13": f_fields.Float(
        required=False, description="Eigenvector for first diffraction limit, coord 3"
    ),
    "resolutionEllipsoidAxis21": f_fields.Float(
        required=False, description="Eigenvector for second diffraction limit, coord 1"
    ),
    "resolutionEllipsoidAxis22": f_fields.Float(
        required=False, description="Eigenvector for second diffraction limit, coord 2"
    ),
    "resolutionEllipsoidAxis23": f_fields.Float(
        required=False, description="Eigenvector for second diffraction limit, coord 3"
    ),
    "resolutionEllipsoidAxis31": f_fields.Float(
        required=False, description="Eigenvector for third diffraction limit, coord 1"
    ),
    "resolutionEllipsoidAxis32": f_fields.Float(
        required=False, description="Eigenvector for third diffraction limit, coord 2"
    ),
    "resolutionEllipsoidAxis33": f_fields.Float(
        required=False, description="Eigenvector for third diffraction limit, coord 3"
    ),
    "resolutionEllipsoidValue1": f_fields.Float(
        required=False, description="First (anisotropic) diffraction limit"
    ),
    "resolutionEllipsoidValue2": f_fields.Float(
        required=False, description="Second (anisotropic) diffraction limit"
    ),
    "resolutionEllipsoidValue3": f_fields.Float(
        required=False, description="Third (anisotropic) diffraction limit"
    ),
}


class AutoProcScalingSchema(Schema):
    """Marshmallows schema class representing AutoProcScaling table"""

    autoProcScalingId = ma_fields.Integer()
    autoProcId = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()
    resolutionEllipsoidAxis11 = ma_fields.Float()
    resolutionEllipsoidAxis12 = ma_fields.Float()
    resolutionEllipsoidAxis13 = ma_fields.Float()
    resolutionEllipsoidAxis21 = ma_fields.Float()
    resolutionEllipsoidAxis22 = ma_fields.Float()
    resolutionEllipsoidAxis23 = ma_fields.Float()
    resolutionEllipsoidAxis31 = ma_fields.Float()
    resolutionEllipsoidAxis32 = ma_fields.Float()
    resolutionEllipsoidAxis33 = ma_fields.Float()
    resolutionEllipsoidValue1 = ma_fields.Float()
    resolutionEllipsoidValue2 = ma_fields.Float()
    resolutionEllipsoidValue3 = ma_fields.Float()


f_auto_proc_scaling_schema = api.model("AutoProcScaling", auto_proc_scaling_dict)
ma_auto_proc_scaling_schema = AutoProcScalingSchema()
