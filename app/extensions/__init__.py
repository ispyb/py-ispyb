# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position,wrong-import-order
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


from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.dialects.mysql.types import LONGBLOB

from flask import current_app
from sqlalchemy.exc import InvalidRequestError

from . import api
from .auth import auth_provider
from .flask_sqlalchemy import SQLAlchemy
from .logging import Logging


logging = Logging()
db = SQLAlchemy()
db.ENUM = ENUM
db.LONGBLOB = LONGBLOB


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
        api,
        auth_provider,
        logging,
        db,
    ):
        extension.init_app(app)

def get_db_items(sql_alchemy_model, dict_schema, ma_schema, query_params):
    """Returns resource based on the passed models and query parameter

    Args:
        sql_alchemy_model ([type]): SQLAlchemy ORM model
        dict_schema ([type]): dict with flask fields
        ma_schema ([type]): marshmallows schema
        query_params (dict): query parameters

    Returns:
        dict: {"data": {"total": int, "rows": list},
                "message" : str,
                "error": str
                }
    """
    offset = 0
    limit = current_app.config.get("PAGINATION_ITEMS_LIMIT")
    info_msg = ""
    error_msg = ""

    if "offset" in query_params.keys():
        offset = query_params.get("offset")
    if "limit" in query_params.keys():
        limit = query_params.get("limit")
        
    query = sql_alchemy_model.query
    total = query.count()

    #Filter items based on schema keys    
    schema_keys = {}
    for key in query_params.keys():
        if key in dict_schema.keys():
            schema_keys[key] = query_params.get(key)

    if schema_keys:
        try:
            query = query.filter_by(**schema_keys)
        except InvalidRequestError as ex:
            print(ex)
            error_msg = "Unable to filter items based on query items (%s)" % str(ex)

    query = query.limit(limit).offset(offset)
    items = ma_schema.dump(query, many=True)[0]

    return {
        "data": {"total": total, "rows": items},
        "message": info_msg,
        "error": error_msg
    }

def get_db_item_by_id(sql_alchemy_model, ma_schema, item_id_dict):
    """Returns data base item by its Id

    Args:
        item_id (int): 

    Returns:
        dict: info dict
    """
    db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
    db_item_json = ma_schema.dump(db_item)[0]

    return db_item_json

def add_db_item(sql_alchemy_model, data):
    """Adds item to db

    Args:
        sql_alchemy_model ([type]): [description]
        data (dict): [description]

    Returns:
        SQLAlchemy db item: [description]
    """
    item = None
    try:
        item = sql_alchemy_model(data)
        db.session.add(item)
        db.session.commit()
    except BaseException as ex:
        print(ex)
        # app.logger.exception(str(ex))
        db.session.rollback()
    return item
