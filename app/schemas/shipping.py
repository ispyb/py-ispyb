"""
ISPyB flask server
"""


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

shipping_dict = {
        'shippingId': f_fields.Integer(required=True, description=''),
        'proposalId': f_fields.Integer(required=True, description=''),
        'shippingName': f_fields.String(required=False, description=''),
        'deliveryAgent_agentName': f_fields.String(required=False, description=''),
        'deliveryAgent_shippingDate': f_fields.String(required=False, description=''),
        'deliveryAgent_deliveryDate': f_fields.String(required=False, description=''),
        'deliveryAgent_agentCode': f_fields.String(required=False, description=''),
        'deliveryAgent_flightCode': f_fields.String(required=False, description=''),
        'shippingStatus': f_fields.String(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=False, description=''),
        'laboratoryId': f_fields.Integer(required=False, description=''),
        'isStorageShipping': f_fields.Integer(required=False, description=''),
        'creationDate': f_fields.DateTime(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'sendingLabContactId': f_fields.Integer(required=False, description=''),
        'returnLabContactId': f_fields.Integer(required=False, description=''),
        'returnCourier': f_fields.String(required=False, description=''),
        'dateOfShippingToUser': f_fields.DateTime(required=False, description=''),
        'shippingType': f_fields.String(required=False, description=''),
        'safetyLevel': f_fields.String(required=False, description=''),
        'deliveryAgent_label': f_fields.String(required=False, description=''),
        'readyByTime': f_fields.String(required=False, description=''),
        'closeTime': f_fields.String(required=False, description=''),
        'physicalLocation': f_fields.String(required=False, description=''),
        'deliveryAgent_pickupConfirmationTimestamp': f_fields.DateTime(required=False, description=''),
        'deliveryAgent_pickupConfirmation': f_fields.String(required=False, description=''),
        'deliveryAgent_readyByTime': f_fields.String(required=False, description=''),
        'deliveryAgent_callinTime': f_fields.String(required=False, description=''),
        'deliveryAgent_productcode': f_fields.String(required=False, description=''),
        'deliveryAgent_flightCodePersonId': f_fields.Integer(required=False, description=''),
        'deliveryAgent_flightCodeTimestamp': f_fields.DateTime(required=False, description=''),
        }

class ShippingSchema(Schema):
    """Marshmallows schema class representing Shipping table"""

    shippingId = ma_fields.Integer()
    proposalId = ma_fields.Integer()
    shippingName = ma_fields.String()
    deliveryAgent_agentName = ma_fields.String()
    deliveryAgent_shippingDate = ma_fields.String()
    deliveryAgent_deliveryDate = ma_fields.String()
    deliveryAgent_agentCode = ma_fields.String()
    deliveryAgent_flightCode = ma_fields.String()
    shippingStatus = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    laboratoryId = ma_fields.Integer()
    isStorageShipping = ma_fields.Integer()
    creationDate = ma_fields.DateTime()
    comments = ma_fields.String()
    sendingLabContactId = ma_fields.Integer()
    returnLabContactId = ma_fields.Integer()
    returnCourier = ma_fields.String()
    dateOfShippingToUser = ma_fields.DateTime()
    shippingType = ma_fields.String()
    safetyLevel = ma_fields.String()
    deliveryAgent_label = ma_fields.String()
    readyByTime = ma_fields.String()
    closeTime = ma_fields.String()
    physicalLocation = ma_fields.String()
    deliveryAgent_pickupConfirmationTimestamp = ma_fields.DateTime()
    deliveryAgent_pickupConfirmation = ma_fields.String()
    deliveryAgent_readyByTime = ma_fields.String()
    deliveryAgent_callinTime = ma_fields.String()
    deliveryAgent_productcode = ma_fields.String()
    deliveryAgent_flightCodePersonId = ma_fields.Integer()
    deliveryAgent_flightCodeTimestamp = ma_fields.DateTime()

f_shipping_schema = api.model('Shipping', shipping_dict)
ma_shipping_schema = ShippingSchema()

