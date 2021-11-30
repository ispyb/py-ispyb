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


from flask_restx._http import HTTPStatus

from pyispyb.app.extensions import db
from pyispyb.app.extensions.authentication import authentication_provider 
from pyispyb.app.utils import create_response_item

from pyispyb.core import models, schemas
from pyispyb.core.modules import contacts, session


def get_proposals_by_query(query_dict):
    """Returns proposal db items

    Args:
        query_dict (dict, optional): [description]. Defaults to {}.

    Returns:
        [type]: [description]
    """
    return db.get_db_items(
        models.Proposal,
        schemas.proposal.dict_schema,
        schemas.proposal.ma_schema,
        query_dict,
    )

def get_proposals_has_person_by_query(query_dict):
    return db.get_db_items(
        models.ProposalHasPerson,
        schemas.proposal_has_person.dict_schema,
        schemas.proposal_has_person.ma_schema,
        query_dict,
    )

def get_proposal_by_id(proposal_id):
    """
    Returns proposal by its proposalId.

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    id_dict = {"proposalId": proposal_id}
    return db.get_db_item(
        models.Proposal, schemas.proposal.ma_schema, id_dict
    )


def get_proposal_info_by_id(proposal_id):
    """
    Returns proposal by its proposalId.

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    proposal_json = get_proposal_by_id(proposal_id)

    person_json = contacts.get_person_by_id(proposal_json["personId"])
    proposal_json["person"] = person_json

    sessions_json = session.get_sessions({"proposalId": proposal_id})
    proposal_json["sessions"] = sessions_json

    return proposal_json


def add_proposal(data_dict):
    """
    Adds a proposal.

    Args:
        proposal_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Proposal, schemas.proposal.ma_schema, data_dict)


def update_proposal(proposal_id, data_dict):
    """
    Updates proposal.

    Args:
        proposal_id ([type]): [description]
        proposal_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"proposalId": proposal_id}
    return db.update_db_item(
        models.Proposal, schemas.proposal.ma_schema, id_dict, data_dict
    )


def patch_proposal(proposal_id, proposal_dict):
    """
    Patch a proposal.

    Args:
        proposal_id ([type]): [description]
        proposal_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"proposalId": proposal_id}
    return db.patch_db_item(
        models.Proposal, schemas.proposal.ma_schema, id_dict, proposal_dict
    )


def delete_proposal(proposal_id):
    """
    Deletes proposal item from db.

    Args:
        proposal_id (int): proposalId column in db

    Returns:
        bool: True if the proposal exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"proposalId": proposal_id}
    return db.delete_db_item(models.Proposal, id_dict)


def get_proposal_ids_by_person_id(person_id):
    proposal_id_list = []
    proposal_dict = get_proposals_by_query({"personId": person_id})
    if proposal_dict["data"]["rows"]:
        for proposal in proposal_dict["data"]["rows"]:
            proposal_id_list.append(proposal["proposalId"])
    proposal_has_person_dict = get_proposals_has_person_by_query(
        {"personId": person_id}
    )
    if proposal_has_person_dict["data"]["rows"]:
        for proposal in proposal_has_person_dict["data"]["rows"]:
            proposal_id_list.append(proposal["proposalId"])
    return proposal_id_list

def get_proposal_ids(request):
    """
    Checks if user can run query.
    Manager role allows to run query without restrictions.
    Otherwise proposal with proposalId in the query parameters should belong
    to the user calling the requests

    Args:
        request (request): [description]

    Returns:
        bool, str: true if user can run query, if False then msg describes the reason
    """

    user_info = authentication_provider.get_user_info_from_auth_header(
        request.headers.get("Authorization")
    )
    
    if user_info["is_admin"]:
        proposal_dict = get_proposals_by_query({})
        proposal_ids = []
        for proposal in proposal_dict["data"]["rows"]:
            proposal_ids.append(proposal["proposalId"])
        return proposal_ids
    else:
        person_id = contacts.get_person_id_by_login(user_info["sub"])
        return get_proposal_ids_by_person_id(person_id)
