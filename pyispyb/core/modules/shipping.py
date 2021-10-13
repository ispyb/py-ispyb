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


from pyispyb.app.extensions import db
from pyispyb.app.utils import create_response_item

from pyispyb.core import models, schemas
from pyispyb.core.modules import contacts, proposal, dewar


def get_shippings(request):
    """Returns shippings by query parameters"""

    query_params = request.args.to_dict()

    run_query, msg = proposal.get_proposal_ids(request)

    if run_query:
        return db.get_db_items(
            models.Shipping,
            schemas.shipping.dict_schema,
            schemas.shipping.ma_schema,
            query_params,
        )
    else:
        return create_response_item(msg=msg)


def get_shipping_by_id(shipping_id):
    """
    Returns shipping by its shippingId.

    Args:
        shipping_id (int): corresponds to shippingId in db

    Returns:
        dict: info about shipping as dict
    """
    id_dict = {"shippingId": shipping_id}
    return db.get_db_item_by_params(
        models.Shipping, schemas.shipping.ma_schema, id_dict
    )


def get_shipping_info_by_id(shipping_id):
    """
    Returns shipping by its shippingId.

    Args:
        shipping_id (int): corresponds to shippingId in db

    Returns:
        dict: info about shipping as dict
    """
    shipping_dict = {}

    shipping_dict["shipping"] = get_shipping_by_id(shipping_id)
    shipping_dict["proposal"] = proposal.get_proposal_by_id(shipping_dict["proposalId"])
    shipping_dict["send_lab_contact"] = contacts.get_lab_contact_by_params(
        {"labContactId": shipping_dict["sendingLabContactId"]}
    )
    shipping_dict["send_person"] = contacts.get_person_by_params(
        {"personId": shipping_dict["send_lab_contact"]["personId"]}
    )
    shipping_dict["send_lab"] = contacts.get_laboratory_by_id(
        shipping_dict["send_person"]["laboratoryId"]
    )
    dewars = dewar.get_dewars_by_query({"shippingId": shipping_id})
    shipping_dict["dewars"] = dewars["data"]["rows"]

    return shipping_dict


def add_shipping(data_dict):
    """
    Adds new shipping

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Shipping, schemas.shipping.ma_schema, data_dict)


def update_shipping(shipping_id, data_dict):
    """
    Updates shipping.

    Args:
        shipping_id ([type]): [description]
        shipping_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"shippingId": shipping_id}
    return db.update_db_item(
        models.Shipping, schemas.shipping.ma_schema, id_dict, data_dict
    )


def patch_shipping(shipping_id, data_dict):
    """
    Partialy updates shipping.

    Args:
        shipping_id ([type]): [description]
        shipping_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"shippingId": shipping_id}
    return db.patch_db_item(
        models.Shipping, schemas.shipping.ma_schema, id_dict, data_dict
    )


def delete_shipping(shipping_id):
    """
    Deletes shipping item from db.

    Args:
        shipping_id (int): shippingId column in db

    Returns:
        bool: True if the shipping exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"shippingId": shipping_id}
    return db.delete_db_item(models.Shipping, id_dict)
