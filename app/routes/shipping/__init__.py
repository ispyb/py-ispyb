# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


import logging
from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.extensions.auth import token_required
from app.modules import shipping


api = Namespace("Shipping", description="Shipping related namespace", path="/shipping")
api_v1.add_namespace(api)


@api.route("/list")
class ShippingList(Resource):
    @api.doc(security="apikey")
    def get(self):
        return shipping.get_all_shippings()


@api.route("/proposal/<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(description="proposal_id should be an integer ")
# @token_required
class ProposalShippingList(Resource):
    def get(self, proposal_id):
        """Returns all proposal shippings"""
        return shipping.get_proposal_shippings(proposal_id)
