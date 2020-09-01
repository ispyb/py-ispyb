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


import sqlite3

from flask import current_app
from sqlalchemy import engine, MetaData
from sqlalchemy.exc import InvalidRequestError
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy


def set_sqlite_pragma(dbapi_connection, connection_record):
    # pylint: disable=unused-argument
    """
    SQLite supports FOREIGN KEY syntax when emitting CREATE statements for
    tables, however by default these constraints have no effect on the
    operation of the table.

    http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#foreign-key-support
    """
    if not isinstance(dbapi_connection, sqlite3.Connection):
        return
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class AlembicDatabaseMigrationConfig(object):
    """
    Helper config holder that provides missing functions of Flask-Alembic
    package since we use custom invoke tasks instead.
    """

    def __init__(self, database, directory="migrations", **kwargs):
        self.db = database  # pylint: disable=invalid-name
        self.directory = directory
        self.configure_args = kwargs


class SQLAlchemy(BaseSQLAlchemy):
    """
    Customized Flask-SQLAlchemy adapter with enabled autocommit, constraints
    auto-naming conventions and ForeignKey constraints for SQLite.
    """

    def __init__(self, *args, **kwargs):
        if "session_options" not in kwargs:
            kwargs["session_options"] = {}
        kwargs["session_options"]["autocommit"] = False
        # Configure Constraint Naming Conventions:
        # http://docs.sqlalchemy.org/en/latest/core/constraints.html#constraint-naming-conventions
        """
        kwargs["metadata"] = MetaData(
            naming_convention={
                "pk": "pk_%(table_name)s",
                "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
                "ix": "ix_%(table_name)s_%(column_0_name)s",
                "uq": "uq_%(table_name)s_%(column_0_name)s",
                "ck": "ck_%(table_name)s_%(constraint_name)s",
            }
        )
        """
        super(SQLAlchemy, self).__init__(*args, **kwargs)

    def init_app(self, app):
        super(SQLAlchemy, self).init_app(app)

        database_uri = app.config["SQLALCHEMY_DATABASE_URI"]
        assert database_uri, "SQLALCHEMY_DATABASE_URI must be configured!"
        if database_uri.startswith("sqlite:"):
            self.event.listens_for(engine.Engine, "connect")(set_sqlite_pragma)

        app.extensions["migrate"] = AlembicDatabaseMigrationConfig(
            self, compare_type=True
        )

    def get_db_items(self, sql_alchemy_model, dict_schema, ma_schema, query_params):
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

    
    def get_db_item_by_id(self, sql_alchemy_model, ma_schema, item_id_dict):
        """Returns data base item by its Id

        Args:
            item_id (int): 

        Returns:
            dict: info dict
        """
        db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
        db_item_json = ma_schema.dump(db_item)[0]

        return db_item_json

    def add_db_item(self, sql_alchemy_model, data):
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
            self.session.add(item)
            self.session.commit()
        except BaseException as ex:
            print(ex)
            # app.logger.exception(str(ex))
            self.session.rollback()
        return item

    def update_db_item(self, sql_alchemy_model, item_id_dict, item_update_dict):
        db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
        if not db_item:
            return None
        else:
            # Do something
            return True


    def patch_db_item(self, sql_alchemy_model, item_id_dict, item_update_dict):
        db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
        if not db_item:
            return None
        else:
            for key, value in item_update_dict.items():
                if hasattr(db_item, key):
                    setattr(db_item, key, value)
                else:
                    print("Attribute %s not defined in the item model" % key)
            self.session.commit()
            return True


    def delete_db_item(self, sql_alchemy_model, item_id_dict):
        db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
        if not db_item:
            return None
        else:
            try:
                self.session.delete(db_item)
                self.session.commit()
                return True
            except Exception as ex:
                print(ex)
                #log.exception(str(ex))
                self.session.rollback()

