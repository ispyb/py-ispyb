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
from pyispyb.core.modules import data_collections

############################
#          MOVIES          #
############################


def get_movies_data_by_dataCollection_id(proposal_id, dataCollection_id):
    sql = getSQLQuery(
        "em/movie", append=" where Movie_dataCollectionId = :dataCollectionId and Proposal_proposalId=:proposalId")
    sql = sql.bindparams(dataCollectionId=dataCollection_id,
                         proposalId=proposal_id)
    res = db.engine.execute(sql)
    return queryResultToDict(res)


def get_movie_thumbnails(proposal_id, movie_id):
    sql = getSQLQuery(
        "em/movie_thumbnails")
    sql = sql.bindparams(movieId=movie_id,
                         proposalId=proposal_id)
    res = db.engine.execute(sql)
    res = queryResultToDict(res)
    if len(res) > 0:
        return queryResultToDict(res)[0]
    return None


############################
#          STATS           #
############################


def get_stats_by_session_id(session_id):
    sql = getSQLQuery(
        "em/sessionStats", append=" where sessionId = :sessionId")
    sql = sql.bindparams(sessionId=session_id)
    res = db.engine.execute(sql)
    return queryResultToDict(res)


def get_stats_by_data_collections_ids(proposal_id, data_collection_ids):
    sql = getSQLQuery("em/dataCollectionsStats",
                      append=" where dataCollectionId in (:dataCollectionIdList) and BLSession.proposalId=:proposalId")
    sql = sql.bindparams(
        dataCollectionIdList=data_collection_ids, proposalId=proposal_id)
    res = db.engine.execute(sql)
    return queryResultToDict(res)


def get_stats_by_data_collections_group_id(proposal_id, data_collection_group_id):
    sql = getSQLQuery("em/dataCollectionsStats",
                      append=" where DataCollection.dataCollectionGroupId=:dataCollectionGroupId and BLSession.proposalId=:proposalId")
    sql = sql.bindparams(
        dataCollectionGroupId=data_collection_group_id, proposalId=proposal_id)
    res = db.engine.execute(sql)
    return queryResultToDict(res)

############################
#     DATA COLLECTION      #
############################


def get_data_collections_groups(proposal_id, session_id):
    res = data_collections.get_data_collections_groups(session_id)
    for row in res:
        row["stats"] = get_stats_by_data_collections_group_id(
            proposal_id,
            row["DataCollectionGroup_dataCollectionGroupId"]
        )
    return res
