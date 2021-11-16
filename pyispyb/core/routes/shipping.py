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
import logging

from flask import current_app, request, send_from_directory
from flask_restx._http import HTTPStatus

from pyispyb.flask_restx_patched import Resource
from pyispyb.app.extensions.auth import token_required, authorization_required
from pyispyb.app.extensions.api import api_v1, Namespace

from pyispyb.core.modules import container, dewar, shipping
from pyispyb.core.schemas import container as container_schemas
from pyispyb.core.schemas import dewar as dewar_schemas
from pyispyb.core.schemas import shipping as shipping_schemas


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)

api = Namespace(
    "Shippings", description="shipping related namespace", path="/shippings"
)
api_v1.add_namespace(api)


@api.route("", endpoint="shippings")
@api.doc(security="apikey")
class Shippings(Resource):
    """Allows to get all shippings"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of shippings"""
        return shipping.get_shippings(request), HTTPStatus.OK

    @token_required
    @authorization_required
    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=201)
    def post(self):
        """Adds a new shipping"""
        return shipping.add_shipping(api.payload)


@api.route("/<int:shipping_id>", endpoint="shipping_by_id")
@api.param("shipping_id", "shipping id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="shipping not found.")
class ShippingById(Resource):
    """Allows to get/set/delete a shipping"""

    @token_required
    @authorization_required
    @api.doc(description="shipping_id should be an integer ")
    @api.marshal_with(shipping_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self, shipping_id):
        """Returns a shipping by shippingId"""
        return shipping.get_shipping_by_id(shipping_id)

    @token_required
    @authorization_required
    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=HTTPStatus.CREATED)
    def put(self, shipping_id):
        """Fully updates shipping with id shipping_id"""
        return shipping.update_shipping(shipping_id, api.payload)

    @token_required
    @authorization_required
    @api.expect(shipping_schemas.f_schema)
    @api.marshal_with(shipping_schemas.f_schema, code=HTTPStatus.CREATED)
    def patch(self, shipping_id):
        """Partially updates shipping with id shipping_id"""
        return shipping.patch_shipping(shipping_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, shipping_id):
        """Deletes shipping by shipping_id"""
        return shipping.delete_shipping(shipping_id)


@api.route("/<int:shipping_id>/info", endpoint="shipping_info_by_id")
@api.param("shipping_id", "shipping id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="shipping not found.")
class ShippingInfoById(Resource):
    """Returns full information of a shipping"""

    @token_required
    @authorization_required
    @api.doc(description="shipping_id should be an integer ")
    # @api.marshal_with(shipping_desc_f_schema)
    def get(self, shipping_id):
        """Returns a full description of a shipping by shippingId"""
        return shipping.get_shipping_info_by_id(shipping_id)


@api.route("/dewars", endpoint="dewars")
@api.doc(security="apikey")
class Dewars(Resource):
    """Dewars resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all dewars items"""
        query_dict = request.args.to_dict()
        return dewar.get_dewars_by_query(query_dict)

    @token_required
    @authorization_required
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

    @token_required
    @authorization_required
    @api.doc(description="dewar_id should be an integer ")
    @api.marshal_with(dewar_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self, dewar_id):
        """Returns a dewar by dewarId"""
        return dewar.get_dewar_by_id(dewar_id)

    @token_required
    @authorization_required
    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=HTTPStatus.CREATED)
    def put(self, dewar_id):
        """Fully updates dewar with dewar_id"""
        return dewar.update_dewar(dewar_id, api.payload)

    @token_required
    @authorization_required
    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=HTTPStatus.CREATED)
    def patch(self, dewar_id):
        """Partially updates dewar with id dewarId"""
        return dewar.patch_dewar(dewar_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, dewar_id):
        """Deletes a dewar by dewarId"""
        return dewar.delete_dewar(dewar_id)


@api.route("/dewars/<int:dewar_id>/labels", endpoint="dewar_labels_by_id")
@api.param("dewar_id", "Dewar id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Dewar not found.")
class DewarLabelsById(Resource):
    """Returns dewar label pdf"""

    #@token_required
    #@authorization_required
    @api.doc(description="dewar_id should be an integer ")
    def get(self, dewar_id):
        """Returns a dewar labels by dewarId"""
        log.info("Generating pdf labels for dewar %d" % dewar_id)
        html_labels_filename, pdf_labels_filename = dewar.get_dewar_labels_by_id(
            dewar_id
        )
        return send_from_directory(
            current_app.config["TEMP_FOLDER"],
            pdf_labels_filename,
            as_attachment=True
        )


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
    @authorization_required
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

    @token_required
    @authorization_required
    @api.doc(description="container_id should be an integer ")
    @api.marshal_with(container_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self, container_id):
        """Returns a container by container_id"""
        return container.get_container_by_id(container_id)

    @token_required
    @authorization_required
    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=HTTPStatus.CREATED)
    def put(self, container_id):
        """Fully updates container with container_id"""
        return container.update_container(container_id, api.payload)

    @token_required
    @authorization_required
    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=HTTPStatus.CREATED)
    def patch(self, container_id):
        """Partially updates container with id containerId"""
        return container.patch_container(container_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, container_id):
        """Deletes a container by containerId"""
        return container.delete_container(container_id)
