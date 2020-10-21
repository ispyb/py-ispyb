"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""

"""
shipment namespace with enpoint allowing to manipulate shipment items.

Example routes:

[GET]   /ispyb/api/v1/shipments     - Retrieves a list of shipments
[GET]   /ispyb/api/v1//shipments/1  - Retrieves shipment #1
[POST]  /ispyb/api/v1//shipments    - Creates a new shipment
[PUT]   /ispyb/api/v1//shipments/1  - Updates shipment #1
[PATCH] /ispyb/api/v1//shipments/1  - Partially updates shipment #1
[DELETE]/ispyb/api/v1//shipments/1  - Deletes shipment #1
"""


import logging
from flask import request
from flask_restx._http import HTTPStatus
from flask_restx_patched import Resource
from app.extensions.auth import token_required, authorization_required
from app.extensions.api import api_v1, Namespace
from ispyb_core.modules import shipping
from ispyb_core.schemas import shipping as shipping_schemas

__license__ = "LGPLv3+"


log = logging.getLogger(__name__)
api = Namespace(
    "Shipments", description="Shipment related namespace", path="/shipments"
)
api_v1.add_namespace(api)


@api.route("", endpoint="shipments")
@api.doc(security="apikey")
class Shipments(Resource):
    """Allows to get all shipments"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of shipments

        Returns:
            list: list of shipments.
        """
        return shipping.get_shipments(request.args), HTTPStatus.OK

    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new shipment"""
        return shipping.add_shipment(api.payload)


@api.route("/<int:shipment_id>", endpoint="shipment_by_id")
@api.param("shipment_id", "shipment id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="shipment not found.")
class ShipmentById(Resource):
    """Allows to get/set/delete a shipment"""

    @api.doc(description="shipment_id should be an integer ")
    @api.marshal_with(shipping_schemas.f_schema, skip_none=True, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, shipment_id):
        """Returns a shipment by shipmentId"""
        return shipping.get_shipment_by_id(shipment_id)

    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, shipment_id):
        """Fully updates shipment with id shipment_id

        Args:
            shipment_id (int): corresponds to shipmentId in db
        """
        log.info("Update shipment %d" % shipment_id)
        return shipping.update_shipment(shipment_id, api.payload)

    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, shipment_id):
        """Partially updates shipment with id shipment_id

        Args:
            shipment_id (int): corresponds to shipmentId in db
        """
        log.info("Patch shipment %d" % shipment_id)
        return shipping.patch_shipment(shipment_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, shipment_id):
        """Deletes shipment by shipment_id

        Args:
            shipment_id (int): corresponds to shipmentId in db

        Returns:
            json, status_code:
        """
        return shipping.delete_shipment(shipment_id)


@api.route("/<int:shipment_id>/info", endpoint="shipment_info_by_id")
@api.param("shipment_id", "shipment id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="shipment not found.")
class ShipmentInfoById(Resource):
    """Returns full information of a shipment"""

    @api.doc(description="shipment_id should be an integer ")
    # @api.marshal_with(shipment_desc_f_schema)
    @token_required
    @authorization_required
    def get(self, shipment_id):
        """Returns a full description of a shipment by shipmentId"""
        return shipping.get_shipment_info_by_id(shipment_id)
