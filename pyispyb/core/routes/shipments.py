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

from flask import request
from flask_restx._http import HTTPStatus
from pyispyb.flask_restx_patched import Resource
from pyispyb.app.extensions.auth import token_required, authorization_required
from pyispyb.app.extensions.api import api_v1, Namespace

from pyispyb.core.modules import container, dewar, shipping
from pyispyb.core.schemas import container as container_schemas
from pyispyb.core.schemas import dewar as dewar_schemas
from pyispyb.core.schemas import shipping as shipping_schemas


__license__ = "LGPLv3+"


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
        """Returns list of shipments"""
        return shipping.get_shipments(request), HTTPStatus.OK

    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=201)
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
    @api.marshal_with(shipping_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
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
        """Fully updates shipment with id shipment_id"""
        return shipping.update_shipment(shipment_id, api.payload)

    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, shipment_id):
        """Partially updates shipment with id shipment_id"""
        return shipping.patch_shipment(shipment_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, shipment_id):
        """Deletes shipment by shipment_id"""
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


@api.route("/dewars", endpoint="dewars")
@api.doc(security="apikey")
class Dewars(Resource):
    """Dewars resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all dewars items"""
        return dewar.get_dewars(request)

    @token_required
    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=201)
    def post(self):
        """Adds a new dewar item"""
        return dewar.add_dewar(api.payload)


@api.route("/dewars/<int:dewar_id>", endpoint="dewar_by_id")
@api.param("dewar_id", "Dewar id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Dewar not found.")
class DewarById(Resource):
    """Allows to get/set/delete a dewar item"""

    @api.doc(description="dewar_id should be an integer ")
    @api.marshal_with(dewar_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, dewar_id):
        """Returns a dewar by dewarId"""
        return dewar.get_dewar_by_id(dewar_id)

    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, dewar_id):
        """Fully updates dewar with dewar_id"""
        return dewar.update_dewar(dewar_id, api.payload)

    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, dewar_id):
        """Partially updates dewar with id dewarId"""
        return dewar.patch_dewar(dewar_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, dewar_id):
        """Deletes a dewar by dewarId"""
        return dewar.delete_dewar(dewar_id)


@api.route("/containers", endpoint="containers")
@api.doc(security="apikey")
class Containers(Resource):
    """Containers resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all container items"""
        return container.get_containers(request)

    @token_required
    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=201)
    def post(self):
        """Adds a new container item"""
        return container.add_container(api.payload)


@api.route("/containers/<int:container_id>", endpoint="container_by_id")
@api.param("container_id", "Container id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Container not found.")
class ContainerById(Resource):
    """Allows to get/set/delete a container item"""

    @api.doc(description="container_id should be an integer ")
    @api.marshal_with(container_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, container_id):
        """Returns a container by container_id"""
        return container.get_container_by_id(container_id)

    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, container_id):
        """Fully updates container with container_id"""
        return container.update_container(container_id, api.payload)

    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, container_id):
        """Partially updates container with id containerId"""
        return container.patch_container(container_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, container_id):
        """Deletes a container by containerId"""
        return container.delete_container(container_id)
