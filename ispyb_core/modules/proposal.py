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

from app.extensions import db, get_resource, add_resource
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

    return get_resource(
        ProposalModel, proposal_dict_schema, proposal_ma_schema, query_params
    )


def get_proposal_by_id(proposal_id):
    """Returns proposal by its proposalId

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    proposal = ProposalModel.query.filter_by(proposalId=proposal_id).first()
    proposal_json = proposal_ma_schema.dump(proposal)[0]

    return proposal_json


# TODO maybe keep just get_proposal_info_by_id and filter results based on api.mode


def get_proposal_info_by_id(proposal_id):
    """Returns proposal by its proposalId

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    proposal = ProposalModel.query.filter_by(proposalId=proposal_id).first()
    proposal_json = proposal_ma_schema.dump(proposal)[0]

    person_json = person.get_person_by_id(proposal.personId)
    proposal_json["person"] = person_json

    sessions_json = session.get_sessions_by_params({"proposalId": proposal_id})
    proposal_json["sessions"] = sessions_json

    return proposal_json


def get_proposal_item_by_id(proposal_id):
    """Returns proposal by proposalId

    Args:
        proposal_id ([type]): [description]

    Returns:
        [type]: [description]
    """
    return ProposalModel.query.filter_by(proposalId=proposal_id).first()


def get_proposal_from_dict(proposal_dict):
    return ProposalModel(**proposal_dict)


def add_proposal(proposal_dict):
    try:
        proposal_item = ProposalModel(**proposal_dict)
        db.session.add(proposal_item)
        db.session.commit()
        return proposal_item.proposalId
    except BaseException as ex:
        print(ex)
        log.exception(str(ex))
        db.session.rollback()


def update_proposal(proposal_id, proposal_dict):
    proposal_item = get_proposal_item_by_id(proposal_id)
    if not proposal_item:
        return None
    else:
        # Do something
        return True


def patch_proposal(proposal_id, proposal_dict):
    proposal_item = get_proposal_item_by_id(proposal_id)
    if not proposal_item:
        return None
    else:
        for key, value in proposal_dict.items():
            if hasattr(proposal_item, key):
                setattr(proposal_item, key, value)
            else:
                print("Attribute %s not defined in the Proposal model" % key)
        db.session.commit()
        return True


def delete_proposal(proposal_id):
    """Deletes proposal item from db

    Args:
        proposal_id (int): proposalId column in db

    Returns:
        bool: True if the proposal exists and deleted successfully,
        otherwise return False
    """
    try:
        proposal_item = get_proposal_item_by_id(proposal_id)
        if not proposal_item:
            return None
        else:
            db.session.delete(proposal_item)
            db.session.commit()
            return True
    except Exception as ex:
        print(ex)
        log.exception(str(ex))
        db.session.rollback()
