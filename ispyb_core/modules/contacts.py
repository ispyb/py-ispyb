"""
Project: py-ispyb
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

from ispyb_core import models, schemas


def get_persons(request):
    """Returns persons by query parameters"""

    query_params = request.args.to_dict()

    return db.get_db_items(
        models.Person,
        schemas.person.dict_schema,
        schemas.person.ma_schema,
        query_params
    )


def get_person_by_params(param_dict):
    """Returns person by its id

    Args:
        person_id (int): corresponds to personId in db

    Returns:
        dict: info about person as dict
    """
    return db.get_db_item_by_params(
        models.Person,
        schemas.person.ma_schema,
        param_dict
        )

def get_person_id_by_login(login_name):
    """Returns person by login name.

    Args:
        login_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    if login_name:
        person_item = get_person_by_params({"login" : login_name})
        if person_item:
            return person_item["personId"]

def add_person(data_dict):
    """Adds person item to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.Person,
        schemas.person.ma_schema,
        data_dict
        )

def get_lab_contacts(request):
    """Returns shipments by query parameters"""

    query_params = request.args.to_dict()
    
    return db.get_db_items(
        models.LabContact,
        schemas.lab_contact.dict_schema,
        schemas.lab_contact.ma_schema,
        query_params
    )


def get_lab_contact_by_id(lab_contact_id):
    """Returns shipment by its shipmentId.

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    param_dict = {"shippingId": lab_contact_id}
    return db.get_db_item_by_params(
        models.LabContact,
        schemas.lab_contact.ma_schema,
        param_dict
        )


def add_lab_contact(data_dict):
    """Adds a new lab contact.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.LabContact,
        schemas.lab_contact.ma_schema,
        data_dict
        )


