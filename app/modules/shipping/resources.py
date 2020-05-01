from flask_restx import Namespace, Resource
from app.models import Shipping as ShippingModel
from app.modules.shipping.schemas import f_shipping_schema, ma_shipping_schema

api = Namespace("Shipping", description="Shipping related namespace", path="/shipping")


@api.route("")
class ShippingList(Resource):
    @api.doc(security="apikey")
    def get(self):
        shipping_list = ShippingModel.query.all()
        return ma_shipping_schema.dump(shipping_list)
