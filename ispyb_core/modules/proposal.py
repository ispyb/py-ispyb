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


import logging

from flask import current_app

from sqlalchemy.exc import InvalidRequestError

from app.extensions import get_db_items, get_db_item_by_id, add_db_item, patch_db_item, update_db_item, delete_db_item
from ispyb_core.models import Proposal as ProposalModel
from ispyb_core.modules import person, session
from ispyb_core.schemas.proposal import proposal_ma_schema, proposal_dict_schema


log = logging.getLogger(__name__)


def get_proposals(query_params):
    """Returns proposals by query parameters"""

    if "login_name" in query_params:
        print(person.get_person_id_by_login(query_params.get("login_name")))
        query_params = query_params.to_dict()
        query_params["personId"] = person.get_person_id_by_login(
            query_params.get("login_name")
        )

    return get_db_items(
        ProposalModel, proposal_dict_schema, proposal_ma_schema, query_params
    )


def get_proposal_by_id(proposal_id):
    """Returns proposal by its proposalId

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    return get_db_item_by_id(ProposalModel, proposal_ma_schema, {"proposalId": proposal_id})

def get_proposal_info_by_id(proposal_id):
    """Returns proposal by its proposalId

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    proposal_json = get_proposal_by_id(proposal_id)

    person_json = person.get_person_by_id(proposal.personId)
    proposal_json["person"] = person_json

    sessions_json = session.get_sessions({"proposalId": proposal_id})
    proposal_json["sessions"] = sessions_json

    return proposal_json


def add_proposal(proposal_dict):
    return add_db_item(ProposalModel, proposal_dict)

def update_proposal(proposal_id, proposal_dict):
    return update_db_item(ProposalModel, {"proposalId": proposal_id}, proposal_dict)

def patch_proposal(proposal_id, proposal_dict):
    return patch_db_item(ProposalModel, {"proposalId": proposal_id}, proposal_dict)


def delete_proposal(proposal_id):
    """Deletes proposal item from db

    Args:
        proposal_id (int): proposalId column in db

    Returns:
        bool: True if the proposal exists and deleted successfully,
        otherwise return False
    """
    return delete_db_item(ProposalModel, {"proposalId": proposal_id})
