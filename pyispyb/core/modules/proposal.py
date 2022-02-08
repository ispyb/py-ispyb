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

from pyispyb.app.utils import getSQLQuery, queryResultToDict

from pyispyb.core import models, schemas


def get_proposals_infos_login(login):
    """
    Returns proposal info list.

    Returns:
        [type]: [description]
    """

    sql = getSQLQuery("proposal/proposalsInfosLogin")
    sql = sql.bindparams(login=login)
    res = db.engine.execute(sql)
    return queryResultToDict(res)


def get_proposals_infos_all():
    """
    Returns proposal info list.

    Returns:
        [type]: [description]
    """

    sql = getSQLQuery("proposal/proposalsInfosAll")
    res = db.engine.execute(sql)
    return queryResultToDict(res)


def get_proposal_infos(proposal_id):
    return {
        "proposal": db.get_db_items(
            models.Proposal,
            schemas.proposal.dict_schema,
            schemas.proposal.ma_schema,
            {'proposalId': proposal_id},
        )["data"]["rows"]
    }


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


def loginAuthorizedForProposal(login, proposalId):
    sql = getSQLQuery("proposal/loginAuthorizedProposal")
    sql = sql.bindparams(login=login, proposalId=proposalId)
    isAuthorized = db.engine.execute(sql)
    return isAuthorized.first()[0] > 0


def findProposalId(idOrName):
    sql = getSQLQuery("proposal/findProposalId")
    sql = sql.bindparams(name=idOrName)
    res = db.engine.execute(sql)
    res = queryResultToDict(res)
    if len(res) == 1:
        return res[0]["proposalId"]
    if len(res) > 1:
        raise Exception(f"More than one proposal found for {idOrName}")
    if len(res) > 1:
        raise Exception(f"No proposal found for {idOrName}")
    return None
