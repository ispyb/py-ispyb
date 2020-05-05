"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

auto_proc_program_dict = {
    "autoProcProgramId": f_fields.Integer(
        required=True, description="Primary key (auto-incremented)"
    ),
    "dataCollectionId": f_fields.Integer(required=False, description=""),
    "processingCommandLine": f_fields.String(
        required=False, description="Command line for running the automatic processing"
    ),
    "processingPrograms": f_fields.String(
        required=False, description="Processing programs (comma separated)"
    ),
    "processingStatus": f_fields.String(
        required=False,
        description="success (1) / fail (0)enum(RUNNING,FAILED,SUCCESS,0,1)",
    ),
    "processingMessage": f_fields.String(
        required=False, description="warning, error,..."
    ),
    "processingStartTime": f_fields.DateTime(
        required=False, description="Processing start time"
    ),
    "processingEndTime": f_fields.DateTime(
        required=False, description="Processing end time"
    ),
    "processingEnvironment": f_fields.String(
        required=False, description="Cpus, Nodes,..."
    ),
    "recordTimeStamp": f_fields.DateTime(
        required=False, description="Creation or last update date/time"
    ),
    "processingJobId": f_fields.Integer(required=True, description=""),
}


class AutoProcProgramSchema(Schema):
    """Marshmallows schema class representing AutoProcProgram table"""

    autoProcProgramId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    processingCommandLine = ma_fields.String()
    processingPrograms = ma_fields.String()
    processingStatus = ma_fields.String()
    processingMessage = ma_fields.String()
    processingStartTime = ma_fields.DateTime()
    processingEndTime = ma_fields.DateTime()
    processingEnvironment = ma_fields.String()
    recordTimeStamp = ma_fields.DateTime()
    processingJobId = ma_fields.Integer()


f_auto_proc_program_schema = api.model("AutoProcProgram", auto_proc_program_dict)
ma_auto_proc_program_schema = AutoProcProgramSchema()
