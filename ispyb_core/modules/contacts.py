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

from ispyb_core.models import LabContact, Laboratory, Person
from ispyb_core.schemas.lab_contact import lab_contact_dict_schema, lab_contact_ma_schema
from ispyb_core.schemas.person import person_f_schema, person_dict_schema, person_ma_schema

def get_persons(query_params):
    """Returns persons by query parameters"""

    return db.get_db_items(
        Person, person_dict_schema, person_ma_schema, query_params
    )


def get_person_by_params(param_dict):
    """Returns person by its id

    Args:
        person_id (int): corresponds to personId in db

    Returns:
        dict: info about person as dict
    """
    return db.get_db_item_by_params(Person, person_ma_schema, param_dict)

def get_person_id_by_login(login_name):
    if login_name:
        person_item = get_person_by_params({"login" : login_name})
        if person_item:
            return person_item["personId"]

def add_person(person_dict):
    return db.add_db_item(Person, person_ma_schema, person_dict)

def get_lab_contacts(query_params):
    """Returns shipments by query parameters"""

    return db.get_db_items(
        LabContact, lab_contact_dict_schema, lab_contact_ma_schema, query_params
    )


def get_lab_contact_by_id(lab_contact_id):
    """Returns shipment by its shipmentId

    Args:
        shipment_id (int): corresponds to shipmentId in db

    Returns:
        dict: info about shipment as dict
    """
    param_dict = {"shippingId": lab_contact_id}
    return db.get_db_item_by_params(LabContact, lab_contact_ma_schema, param_dict)


def add_lab_contact(lab_contact_dict):
    return db.add_db_item(LabContact, lab_contact_ma_schema, lab_contact_dict)


