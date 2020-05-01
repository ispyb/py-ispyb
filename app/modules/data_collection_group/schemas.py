
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

data_collection_group_dict = {
        'dataCollectionGroupId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'blSampleId': f_fields.Integer(required=False, description='references BLSample table'),
        'sessionId': f_fields.Integer(required=True, description='references Session table'),
        'workflowId': f_fields.Integer(required=False, description=''),
        'experimentType': f_fields.String(required=False, description='Experiment type flagenum(EM,SAD,SAD - Inverse Beam,OSC,Collect - Multiwedge,MAD,Helical,Multi-positional,Mesh,Burn,MAD - Inverse Beam,Characterization,Dehydration,Still)'),
        'startTime': f_fields.DateTime(required=False, description='Start time of the dataCollectionGroup'),
        'endTime': f_fields.DateTime(required=False, description='end time of the dataCollectionGroup'),
        'crystalClass': f_fields.String(required=False, description='Crystal Class for industrials users'),
        'comments': f_fields.String(required=False, description='comments'),
        'detectorMode': f_fields.String(required=False, description='Detector mode'),
        'actualSampleBarcode': f_fields.String(required=False, description='Actual sample barcode'),
        'actualSampleSlotInContainer': f_fields.Integer(required=False, description='Actual sample slot number in container'),
        'actualContainerBarcode': f_fields.String(required=False, description='Actual container barcode'),
        'actualContainerSlotInSC': f_fields.Integer(required=False, description='Actual container slot number in sample changer'),
        'xtalSnapshotFullPath': f_fields.String(required=False, description=''),
        }

class DataCollectionGroupSchema(Schema):
    dataCollectionGroupId = ma_fields.Integer()
    blSampleId = ma_fields.Integer()
    sessionId = ma_fields.Integer()
    workflowId = ma_fields.Integer()
    experimentType = ma_fields.String()
    startTime = ma_fields.DateTime()
    endTime = ma_fields.DateTime()
    crystalClass = ma_fields.String()
    comments = ma_fields.String()
    detectorMode = ma_fields.String()
    actualSampleBarcode = ma_fields.String()
    actualSampleSlotInContainer = ma_fields.Integer()
    actualContainerBarcode = ma_fields.String()
    actualContainerSlotInSC = ma_fields.Integer()
    xtalSnapshotFullPath = ma_fields.String()

f_data_collection_group_schema = api.model('DataCollectionGroup', data_collection_group_dict)
ma_data_collection_group_schema = DataCollectionGroupSchema()
