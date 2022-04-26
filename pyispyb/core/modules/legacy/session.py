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


from pyispyb.app.utils import get_sql_query, queryresult_to_dict
from pyispyb.app.extensions.database.middleware import db


def get_session_infos_login(login):
    """Get info for sessions that user can access.

    Args:
        login (str): user login

    Returns:
        list: sessions infos
    """
    sql = get_sql_query("session/sessionsInfosLogin")
    sql = sql.bindparams(login=login)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_session_infos_all(db):
    """Get info for all sessions.

    Returns:
        list: sessions infos
    """
    sql = get_sql_query("session/sessionsInfosAll")
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_session_infos_login_proposal(login, proposal_id):
    """Get info for sessions in proposal that user can access.

    Args:
        login (str): user login
        proposal_id (str): proposal id

    Returns:
        list: sessions infos
    """
    sql = get_sql_query(
        "session/sessionsInfosLogin", append=" and proposalId = :proposalId"
    )
    sql = sql.bindparams(login=login, proposalId=proposal_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_session_infos_all_proposal(proposal_id):
    """Get info for all sessions in proposal.

    Args:
        proposal_id (str): proposal id

    Returns:
        list: sessions infos
    """
    sql = get_sql_query(
        "session/sessionsInfosAll", append=" where proposalId = :proposalId"
    )
    sql = sql.bindparams(proposalId=proposal_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_session_infos_login_dates(login, start_date, end_date):
    """Get info for sessions between dates that user can access.

    Args:
        login (str): user login
        start_date (str): start_date
        end_date (str): end_date

    Returns:
        list: sessions infos
    """
    sql = get_sql_query(
        "session/sessionsInfosLogin",
        append="""
    and (
        (BLSession_startDate >= :startDate and BLSession_startDate <= :endDate)
        or
        (BLSession_endDate >= :startDate and BLSession_endDate <= :endDate)
        or
        (BLSession_endDate >= :endDate and BLSession_startDate <= :startDate)
        or
        (BLSession_endDate <= :endDate and BLSession_startDate >= :startDate)
        )
    order by v_session.sessionId DESC
    """,
    )
    sql = sql.bindparams(login=login, startDate=start_date, endDate=end_date)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_session_infos_all_dates(start_date, end_date):
    """Get info for all sessions between dates.

    Args:
        start_date (str): start_date
        end_date (str): end_date

    Returns:
        list: sessions infos
    """
    sql = get_sql_query(
        "session/sessionsInfosAll",
        append="""
    where (
        (BLSession_startDate >= :startDate and BLSession_startDate <= :endDate)
        or
        (BLSession_endDate >= :startDate and BLSession_endDate <= :endDate)
        or
        (BLSession_endDate >= :endDate and BLSession_startDate <= :startDate)
        or
        (BLSession_endDate <= :endDate and BLSession_startDate >= :startDate)
        )
    order by v_session.sessionId DESC
    """,
    )
    sql = sql.bindparams(startDate=start_date, endDate=end_date)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def login_authorized_for_session(login, session_id):
    """Verify that login is authorized to access session.

    Args:
        login (str): login
        session_id (str): session id

    Returns:
        boolean: authorization
    """
    sql = get_sql_query("session/loginAuthorizedSession")
    sql = sql.bindparams(login=login, sessionId=session_id)
    is_authorized = db.session.execute(sql)
    return is_authorized.first()[0] > 0
