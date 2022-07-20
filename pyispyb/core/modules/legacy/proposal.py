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

from ispyb import models

from pyispyb.app.utils import get_sql_query, queryresult_to_dict
from pyispyb.app.extensions.database.middleware import db


def get_proposals_infos_login(login):
    """
    Get infos for all proposals that user can access.

    Args:
        login (str): user login

    Returns:
        dict: proposal infos
    """
    sql = get_sql_query("proposal/proposalsInfosLogin")
    sql = sql.bindparams(login=login)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_proposals_infos_all():
    """Get infos for all proposals.

    Returns:
        dict: proposal infos
    """
    sql = get_sql_query("proposal/proposalsInfosAll")
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_proposal_infos(proposal_id):
    """Get proposal infos.

    Args:
        proposal_id (str): proposal id

    Returns:
        dict: proposal infos
    """
    return {
        "proposal": (
            db.session.query(models.Proposal)
            .filter(models.Proposal.proposalId == proposal_id)
            .first()
        )
    }


def login_authorized_for_proposal(login, proposal_id):
    """Verify that login is authorized for proposal.

    Args:
        login (str): user login
        proposal_id (str): proposal id

    Returns:
        boolean: authorization
    """
    sql = get_sql_query("proposal/loginAuthorizedProposal")
    sql = sql.bindparams(login=login, proposalId=proposal_id)
    is_authorized = db.session.execute(sql)
    return is_authorized.first()[0] > 0


def find_proposal_id(id_or_name):
    """Convert proposal name to id. If id, return id.

    Args:
        id_or_name (str): proposal id or name

    Raises:
        Exception: More than one proposal found for name
        Exception: No proposal found for name

    Returns:
        str: proposal id
    """
    sql = get_sql_query("proposal/findProposalId")
    sql = sql.bindparams(name=id_or_name)
    res = db.session.execute(sql)
    res = queryresult_to_dict(res)
    if len(res) == 1:
        return res[0]["proposalId"]
    if len(res) > 1:
        raise Exception(f"More than one proposal found for {id_or_name}")
    if len(res) > 1:
        raise Exception(f"No proposal found for {id_or_name}")
    return None
