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

from app.extensions import db
from app.models import Proposal as ProposalModel
from app.modules import person
from app.schemas.proposal import proposal_ma_schema, proposal_dict_schema


log = logging.getLogger(__name__)


def get_proposals(offset, limit):
    """Returns proposals defined by pagination offset and limit

    Args:
        offset (int): pagination offset
        limit (int): if not passed then limit is defined as
        PAGINATION_ITEMS_LIMIT in config.py

    Returns:
        list: list of proposals
    """

    if not offset:
        offset = 1
    if not limit:
        limit = current_app.config["PAGINATION_ITEMS_LIMIT"]

    total = ProposalModel.query.count()
    query = ProposalModel.query.limit(limit).offset(offset)
    proposals = proposal_ma_schema.dump(query, many=True)[
        0
    ]  # Why this is a list of list???

    return {"total": total, "rows": proposals}


def get_proposal_by_id(proposal_id):
    """Returns proposal by its proposalId

    Args:
        proposal_id (int): corresponds to proposalId in db

    Returns:
        dict: info about proposal as dict
    """
    proposal = ProposalModel.query.filter_by(proposalId=proposal_id).first()
    return proposal_ma_schema.dump(proposal)[0]  # Again this...


def get_proposals_by_params(params):
    """Returns list of proposals defined by query parameters

    Args:
        params (dict): query parameters

    Returns:
        list: list of proposals
    """
    query_params = {}
    for key in params.keys():
        if key in proposal_dict_schema.keys():
            query_params[key] = params[key]

    proposal = ProposalModel.query.filter_by(**query_params)
    return proposal_ma_schema.dump(proposal, many=True)[0]


def get_proposal_item_by_id(proposal_id):
    """Returns proposal by proposalId

    Args:
        proposal_id ([type]): [description]

    Returns:
        [type]: [description]
    """
    return ProposalModel.query.filter_by(proposalId=proposal_id).first()


def get_proposals_by_login_name(login_name):
    """Returns proposals by a login name
    """
    person_id = person.get_person_id_by_login(login_name)
    # TODO this is not nice...
    proposal = ProposalModel.query.filter_by(personId=person_id)
    return proposal_ma_schema.dump(proposal, many=True)


def get_proposal_from_dict(proposal_dict):
    return ProposalModel(**proposal_dict)


def add_proposal(proposal_dict):
    try:
        proposal_item = ProposalModel(**proposal_dict)
        db.session.add(proposal_item)
        db.session.commit()
        return proposal_item.proposalId
    except BaseException:
        return
        
def update_proposal(proposal_dict):
    print(proposal_dict)


def delete_proposal(proposal_id):
    """Deletes proposal item from db

    Args:
        proposal_id (int): proposalId column in db

    Returns:
        bool: True if the proposal exists and deleted successfully,
        otherwise return False
    """
    try:
        proposal_item = ProposalModel.query.filter_by(proposalId=proposal_id).first()
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
