"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

auto_proc_scaling_statistics_dict = {
    "autoProcScalingStatisticsId": f_fields.Integer(
        required=True, description="Primary key (auto-incremented)"
    ),
    "autoProcScalingId": f_fields.Integer(
        required=False, description="Related autoProcScaling item (used by foreign key)"
    ),
    "scalingStatisticsType": f_fields.String(
        required=True,
        description="Scaling statistics typeenum(overall,innerShell,outerShell)",
    ),
    "comments": f_fields.String(required=False, description="Comments..."),
    "resolutionLimitLow": f_fields.Float(
        required=False, description="Low resolution limit"
    ),
    "resolutionLimitHigh": f_fields.Float(
        required=False, description="High resolution limit"
    ),
    "rMerge": f_fields.Float(required=False, description="Rmerge"),
    "rMeasWithinIPlusIMinus": f_fields.Float(
        required=False, description="Rmeas (within I+/I-)"
    ),
    "rMeasAllIPlusIMinus": f_fields.Float(
        required=False, description="Rmeas (all I+ & I-)"
    ),
    "rPimWithinIPlusIMinus": f_fields.Float(
        required=False, description="Rpim (within I+/I-) "
    ),
    "rPimAllIPlusIMinus": f_fields.Float(
        required=False, description="Rpim (all I+ & I-)"
    ),
    "fractionalPartialBias": f_fields.Float(
        required=False, description="Fractional partial bias"
    ),
    "nTotalObservations": f_fields.Integer(
        required=False, description="Total number of observations"
    ),
    "nTotalUniqueObservations": f_fields.Integer(
        required=False, description="Total number unique"
    ),
    "meanIOverSigI": f_fields.Float(required=False, description="Mean((I)/sd(I))"),
    "completeness": f_fields.Float(required=False, description="Completeness"),
    "multiplicity": f_fields.Float(required=False, description="Multiplicity"),
    "anomalousCompleteness": f_fields.Float(
        required=False, description="Anomalous completeness"
    ),
    "anomalousMultiplicity": f_fields.Float(
        required=False, description="Anomalous multiplicity"
    ),
    "recordTimeStamp": f_fields.DateTime(
        required=False, description="Creation or last update date/time"
    ),
    "anomalous": f_fields.Integer(
        required=False, description="boolean type:0 noanoum - 1 anoum"
    ),
    "ccHalf": f_fields.Float(required=False, description="information from XDS"),
    "ccAno": f_fields.Float(required=False, description=""),
    "sigAno": f_fields.String(required=False, description=""),
    "isa": f_fields.String(required=False, description=""),
    "completenessSpherical": f_fields.Float(
        required=False,
        description="Completeness calculated assuming isotropic diffraction",
    ),
    "completenessEllipsoidal": f_fields.Float(
        required=False,
        description="Completeness calculated allowing for anisotropic diffraction",
    ),
    "anomalousCompletenessSpherical": f_fields.Float(
        required=False,
        description="Anomalous completeness calculated assuming isotropic diffraction",
    ),
    "anomalousCompletenessEllipsoidal": f_fields.Float(
        required=False,
        description="Anisotropic completeness calculated allowing for anisotropic diffraction",
    ),
    "ccAnomalous": f_fields.Float(required=False, description=""),
}


class AutoProcScalingStatisticsSchema(Schema):
    """Marshmallows schema class representing AutoProcScalingStatistics table"""

    autoProcScalingStatisticsId = ma_fields.Integer()
    autoProcScalingId = ma_fields.Integer()
    scalingStatisticsType = ma_fields.String()
    comments = ma_fields.String()
    resolutionLimitLow = ma_fields.Float()
    resolutionLimitHigh = ma_fields.Float()
    rMerge = ma_fields.Float()
    rMeasWithinIPlusIMinus = ma_fields.Float()
    rMeasAllIPlusIMinus = ma_fields.Float()
    rPimWithinIPlusIMinus = ma_fields.Float()
    rPimAllIPlusIMinus = ma_fields.Float()
    fractionalPartialBias = ma_fields.Float()
    nTotalObservations = ma_fields.Integer()
    nTotalUniqueObservations = ma_fields.Integer()
    meanIOverSigI = ma_fields.Float()
    completeness = ma_fields.Float()
    multiplicity = ma_fields.Float()
    anomalousCompleteness = ma_fields.Float()
    anomalousMultiplicity = ma_fields.Float()
    recordTimeStamp = ma_fields.DateTime()
    anomalous = ma_fields.Integer()
    ccHalf = ma_fields.Float()
    ccAno = ma_fields.Float()
    sigAno = ma_fields.String()
    isa = ma_fields.String()
    completenessSpherical = ma_fields.Float()
    completenessEllipsoidal = ma_fields.Float()
    anomalousCompletenessSpherical = ma_fields.Float()
    anomalousCompletenessEllipsoidal = ma_fields.Float()
    ccAnomalous = ma_fields.Float()


f_auto_proc_scaling_statistics_schema = api.model(
    "AutoProcScalingStatistics", auto_proc_scaling_statistics_dict
)
ma_auto_proc_scaling_statistics_schema = AutoProcScalingStatisticsSchema()
