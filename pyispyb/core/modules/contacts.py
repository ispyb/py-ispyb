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
from pyispyb.app.extensions.auth import auth_provider

from pyispyb.core import models, schemas
from pyispyb.core.modules import proposal, sample, protein, crystal


def get_person_by_id(person_id):
    id_dict = {"personId": person_id}
    return db.get_db_item(
        models.Person, schemas.person.ma_schema, id_dict
    )

def get_person_info(request):
    user_info = auth_provider.get_user_info_from_auth_header(
        request.headers.get("Authorization")
    )
    query_dict = request.args.to_dict()
    if "login_name" in query_dict:
        #Return info about requested login name
        person_id = get_person_id_by_login(query_dict["login_name"])
    else:
        person_id = get_person_id_by_login(user_info["sub"])

    if person_id:
        person_info = get_person_info_by_params({"personId": person_id})
        person_info["personId"] = person_id
        user_info.update(person_info)

    return user_info

def get_person_info_by_params(param_dict):
    """Returns person by its id.

    Args:
        param_dict (dict): corresponds to personId in db

    Returns:
        dict: info about person as dict
    """
    person_info_dict = db.get_db_item(
        models.Person, schemas.person.ma_schema, param_dict
    )
    proposal_id_list = proposal.get_proposal_ids_by_person_id(
        person_info_dict["personId"]
    )
    person_info_dict["proposal_ids"] = proposal_id_list

    person_protein_list = []
    for proposal_id in proposal_id_list:
        protein_list = protein.get_proteins_by_query({"proposalId": proposal_id})
        for protein_dict in protein_list["data"]["rows"]:
            person_protein_list.append(protein_dict["proteinId"])

    # sample_list = sample.get_samples_by_request
    person_info_dict["protein_ids"] = person_protein_list

    return person_info_dict

def get_persons_by_query(query_dict):
    """Returns person by its id.

    Args:
        param_dict (dict): corresponds to personId in db

    Returns:
        dict: info about person as dict
    """
    return db.get_db_items(
        models.Person,
        schemas.person.dict_schema,
        schemas.person.ma_schema,
        query_dict,
    )

def get_person_id_by_login(login_name):
    """Returns person by login name.

    Args:
        login_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    if login_name:
        persons = get_persons_by_query({"login": login_name})["data"]["rows"]
        if persons:
            return persons[0]["personId"]


def add_person(data_dict):
    """Adds person item to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Person, schemas.person.ma_schema, data_dict)


def update_person(person_id, data_dict):
    """
    Updates person.

    Args:
        person_id ([type]): [description]
        person_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"personId": person_id}
    return db.update_db_item(
        models.Person, schemas.person.ma_schema, id_dict, data_dict
    )


def patch_person(person_id, person_dict):
    """
    Patch a person.

    Args:
        person_id ([type]): [description]
        person_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"personId": person_id}
    return db.patch_db_item(
        models.Person, schemas.person.ma_schema, id_dict, person_dict
    )


def delete_person(person_id):
    """Deletes person item from db.

    Args:
        person_id (int): personId column in db

    Returns:
        bool: True if the person exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"personId": person_id}
    return db.delete_db_item(models.Person, id_dict)


def get_lab_contacts(request):
    """Returns lab contact by query parameters"""

    query_dict = request.args.to_dict()

    return db.get_db_items(
        models.LabContact,
        schemas.lab_contact.dict_schema,
        schemas.lab_contact.ma_schema,
        query_dict,
    )


def get_lab_contact_by_params(param_dict):
    """
    Returns lab contacts by params.

    Args:
        param_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.get_db_item(
        models.LabContact, schemas.lab_contact.ma_schema, param_dict
    )


def add_lab_contact(data_dict):
    """
    Adds a new lab contact.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.LabContact, schemas.lab_contact.ma_schema, data_dict)


def update_lab_contact(lab_contact_id, data_dict):
    """
    Updates lab contact.

    Args:
        lab_contact_id (int): [description]
        data_dict (dict): [description]

    Returns:
       dict: [description]
    """
    id_dict = {"labContactId": lab_contact_id}
    return db.update_db_item(
        models.LabContact, schemas.lab_contact.ma_schema, id_dict, data_dict
    )


def patch_lab_contact(lab_contact_id, data_dict):
    """
    Patches lab contact db item.

    Args:
        lab_contact_id (int): [description]
        data_dict (dict): [description]

    Returns:
        dict: [description]
    """
    id_dict = {"labContactId": lab_contact_id}
    return db.patch_db_item(
        models.LabContact, schemas.lab_contact.ma_schema, id_dict, data_dict
    )


def delete_lab_contact(lab_contact_id):
    """
    Deletes lab contact.

    Args:
        lab_contact_id ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"labContactId": lab_contact_id}
    return db.delete_db_item(models.LabContact, id_dict)


def get_laboratories(request):
    """
    Returns laboratories based on query parameters.

    Args:
        query_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    query_dict = request.args.to_dict()

    return db.get_db_items(
        models.Laboratory,
        schemas.laboratory.dict_schema,
        schemas.laboratory.ma_schema,
        query_dict,
    )


def add_laboratory(data_dict):
    """
    Adds new laboratory.

    Args:
        laboratory_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Laboratory, schemas.laboratory.ma_schema, data_dict)


def get_laboratory_by_id(laboratory_id):
    """
    Returns laboratory info by its laboratoryId.

    Args:
        laboratory_id (int): corresponds to laboratoryId in db

    Returns:
        dict: info about laboratory as dict
    """
    data_dict = {"laboratoryId": laboratory_id}
    return db.get_db_item(
        models.Laboratory, schemas.laboratory.ma_schema, data_dict
    )


def patch_laboratory(laboratory_id, data_dict):
    """
    Patch a laboratory.

    Args:
        laboratory_id ([type]): [description]
        laboratory_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"laboratoryId": laboratory_id}
    return db.patch_db_item(
        models.Laboratory, schemas.laboratory.ma_schema, id_dict, data_dict
    )


def update_laboratory(laboratory_id, data_dict):
    """
    Updates laboratory db item.

    Args:
        laboratory_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"laboratoryId": laboratory_id}
    return db.update_db_item(
        models.Laboratory, schemas.laboratory.ma_schema, id_dict, data_dict
    )


def delete_laboratory(laboratory_id):
    """
    Deletes laboratory item from db.

    Args:
        laboratory_id (int): laboratoryId column in db

    Returns:
        bool: True if the laboratory exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"laboratoryId": laboratory_id}
    return db.delete_db_item(models.Laboratory, id_dict)
