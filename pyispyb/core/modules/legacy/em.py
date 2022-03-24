
# Project: py-ispyb.

# https://github.com/ispyb/py-ispyb

# This file is part of py-ispyb software.

# py-ispyb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# py-ispyb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"

from pyispyb.app.utils import get_sql_query, queryresult_to_dict
from pyispyb.app.extensions.database.middleware import db
from pyispyb.core.modules.legacy import data_collections

############################
#          MOVIES          #
############################


def get_movies_data_by_datacollection_id(proposal_id, datacollection_id):
    """Get movies data for datacollection.

    Args:
        proposal_id (str): proposal id
        datacollection_id (str): datacollection id

    Returns:
        dict: movies data
    """
    sql = get_sql_query(
        "em/movie",
        append=" where Movie_dataCollectionId = :dataCollectionId and Proposal_proposalId=:proposalId")
    sql = sql.bindparams(dataCollectionId=datacollection_id,
                         proposalId=proposal_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_movie_thumbnails(proposal_id, movie_id):
    """Get movie thumbnails.

    Args:
        proposal_id (str): proposal id
        movie_id (str): movie id

    Returns:
        dict: thumnails object
    """
    sql = get_sql_query(
        "em/movie_thumbnails")
    sql = sql.bindparams(movieId=movie_id,
                         proposalId=proposal_id)
    res = db.session.execute(sql)
    res = queryresult_to_dict(res)
    if len(res) > 0:
        return queryresult_to_dict(res)[0]
    return None


############################
#          STATS           #
############################


def get_stats_by_session_id(session_id):
    """Get stats for session.

    Args:
        session_id (str): session id

    Returns:
        dict: stats
    """
    sql = get_sql_query(
        "em/sessionStats", append=" where sessionId = :sessionId")
    sql = sql.bindparams(sessionId=session_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_stats_by_data_collections_ids(proposal_id, data_collection_ids):
    """Get stats for data collections.

    Args:
        proposal_id (str): proposal id
        data_collection_ids (str): comma-separated data collection ids

    Returns:
        dict: stats
    """
    sql = get_sql_query(
        "em/dataCollectionsStats",
        append=" where dataCollectionId in (:dataCollectionIdList) and BLSession.proposalId=:proposalId")
    sql = sql.bindparams(
        dataCollectionIdList=data_collection_ids, proposalId=proposal_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)


def get_stats_by_data_collections_group_id(
        proposal_id, data_collection_group_id):
    """Get stats for datacollection group.

    Args:
        proposal_id (str): proposal id
        data_collection_group_id (str): data collection group id

    Returns:
        dict: stats
    """
    sql = get_sql_query(
        "em/dataCollectionsStats",
        append=" where DataCollection.dataCollectionGroupId=:dataCollectionGroupId and BLSession.proposalId=:proposalId")
    sql = sql.bindparams(
        dataCollectionGroupId=data_collection_group_id, proposalId=proposal_id)
    res = db.session.execute(sql)
    return queryresult_to_dict(res)

############################
#     DATA COLLECTION      #
############################


def get_data_collections_groups(proposal_id, session_id):
    """
    Get data collection groups for session.

    Args:
        proposal_id (str): proposal id
        session_id (str): session id

    Returns:
        list: datacollection groups
    """
    res = data_collections.get_data_collections_groups(session_id)
    for row in res:
        row["stats"] = get_stats_by_data_collections_group_id(
            proposal_id,
            row["DataCollectionGroup_dataCollectionGroupId"]
        )
    return res
