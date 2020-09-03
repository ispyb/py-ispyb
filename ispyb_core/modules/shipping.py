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
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from app.extensions import db

from ispyb_core.models import Shipping as ShippingModel
from ispyb_core.schemas.shipping import shipping_dict_schema, shipping_ma_schema


def get_shipments(query_params):
    """Returns shipments by query parameters"""

    return db.get_db_items(
        ShippingModel, shipping_dict_schema, shipping_ma_schema, query_params
    )


def get_shipment_by_id(shipment_id):
    """Returns shipment by its shipmentId

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    id_dict = {"shippingId": shipment_id}
    return db.get_db_item_by_params(ShippingModel, shipping_ma_schema, id_dict)


def get_shipment_info_by_id(shipment_id):
    """Returns shipment by its shipmentId

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    shipment_json = get_shipment_by_id(shipment_id)

    return shipment_json


def add_shipment(shipment_dict):
    return db.add_db_item(ShippingModel, shipping_ma_schema, shipment_dict)


def update_shipment(shipment_id, shipment_dict):
    id_dict = {"shippingId": shipment_id}
    return db.update_db_item(ShippingModel, id_dict, shipment_dict)


def patch_shipment(shipment_id, shipment_dict):
    id_dict = {"shippingId": shipment_id}
    return db.patch_db_item(ShippingModel, id_dict, shipment_dict)


def delete_shipment(shipment_id):
    """Deletes shipment item from db

    Args:
        shipment_id (int): shipmentId column in db

    Returns:
        bool: True if the shipment exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"shippingId": shipment_id}
    return db.delete_db_item(ShippingModel, id_dict)
