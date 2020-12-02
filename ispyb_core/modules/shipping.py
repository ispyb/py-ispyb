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


__license__ = "LGPLv3+"


from app.extensions import db
from app.extensions.auth import auth_provider
from app.utils import create_response_item

from ispyb_core import models, schemas
from ispyb_core.modules import proposal


def get_shipments(request):
    """Returns shipments by query parameters"""

    query_params = request.args.to_dict()

    user_info = auth_provider.get_user_info_by_auth_header(
        request.headers.get("Authorization")
    )

    # If the user has no admin role then allow retreive sessions 
    # from particular proposals
    # 
    # Do we need to retrieve sessions from all proposals?
    # Add sessions from session_has_person
    run_query = False
    msg = None

    if user_info.get("is_admin"):
        run_query = True
    else:
        if "proposalId" not in query_params.keys():
            msg = "User is not admin. No proposalId in query parameters"
        else:
            # Check if proposal belongs to the person
            user_proposals, status_code = proposal.get_proposals(request)
            for user_proposal in user_proposals["data"]["rows"]:
                if user_proposal.get("proposalId") == int(query_params.get("proposalId")):
                    run_query = True
                    break
            
            if not run_query:
                msg = "Proposal with id %s is not associated with user %s" % (
                    query_params.get("proposalId"),
                    user_info.get("username")
                )

    if run_query:
        return db.get_db_items(
            models.Shipping,
            schemas.shipping.dict_schema,
            schemas.shipping.ma_schema,
            query_params,
            )
    else:
        return create_response_item(msg=msg)


def get_shipment_by_id(shipment_id):
    """
    Returns shipment by its shipmentId.

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    id_dict = {"shippingId": shipment_id}
    return db.get_db_item_by_params(
        models.Shipping, schemas.shipping.ma_schema, id_dict
    )


def get_shipment_info_by_id(shipment_id):
    """
    Returns shipment by its shipmentId.

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    shipment_json = get_shipment_by_id(shipment_id)

    return shipment_json


def add_shipment(data_dict):
    """
    Adds new shipment

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Shipping, schemas.shipping.ma_schema, data_dict)


def update_shipment(shipment_id, data_dict):
    """
    Updates shipment.

    Args:
        shipment_id ([type]): [description]
        shipment_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"shippingId": shipment_id}
    return db.update_db_item(
        models.Shipping, schemas.shipping.ma_schema, id_dict, data_dict
    )


def patch_shipment(shipment_id, data_dict):
    """
    Partialy updates shipment.

    Args:
        shipment_id ([type]): [description]
        shipment_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"shippingId": shipment_id}
    return db.patch_db_item(
        models.Shipping, schemas.shipping.ma_schema, id_dict, data_dict
    )


def delete_shipment(shipment_id):
    """
    Deletes shipment item from db.

    Args:
        shipment_id (int): shipmentId column in db

    Returns:
        bool: True if the shipment exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"shippingId": shipment_id}
    return db.delete_db_item(models.Shipping, id_dict)
