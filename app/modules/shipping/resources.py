from flask_restx import Namespace, Resource
from app.models import Shipping as ShippingModel
from app.modules.shipping.schemas import f_shipping_schema, ma_shipping_schema

api = Namespace("Shipping", description="Shipping related namespace", path="/shipping")


def get_all_shippings():
    shipping_list = ShippingModel.query.all()
    return ma_shipping_schema.dump(shipping_list, many=True)


def get_proposal_shippings(proposal_id):
    shipping_list = ShippingModel.query.filter_by(proposalId=proposal_id)
    return ma_shipping_schema.dump(shipping_list, many=True)


@api.route("")
class ShippingList(Resource):
    @api.doc(security="apikey")
    def get(self):
        return get_all_shippings()


@api.route("/proposal/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(description="proposal_id should be an integer ")
# @token_required
class ProposalShippingList(Resource):
    def get(self, proposal_id):
        """Returns all proposal shippings"""
        return get_proposal_shippings(proposal_id)
