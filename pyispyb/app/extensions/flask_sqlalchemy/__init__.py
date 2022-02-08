
# Project: py-ispyb
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


import sqlite3

from flask_restx import abort
from flask_restx._http import HTTPStatus


from flask import current_app
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy

from pyispyb.app.utils import create_response_item


def set_sqlite_pragma(dbapi_connection, connection_record):
    # pylint: disable=unused-argument
    """
    Sqlite supports FOREIGN KEY syntax when emitting CREATE statements for tables.

    By default these constraints have no effect on the
    operation of the table.

    http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#foreign-key-support

    Args:
        dbapi_connection ([type]): [description]
        connection_record ([type]): [description]
    """
    if not isinstance(dbapi_connection, sqlite3.Connection):
        return
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class AlembicDatabaseMigrationConfig:
    """
    Helper config holder that provides missing functions of Flask-Alembic.

    Args:
        object ([type]): [description]
    """

    def __init__(self, database, directory="migrations", **kwargs):
        self.db = database  # pylint: disable=invalid-name
        self.directory = directory
        self.configure_args = kwargs


class SQLAlchemy(BaseSQLAlchemy):
    """
    Customized Flask-SQLAlchemy adapter.

    Args:
        BaseSQLAlchemy ([type]): [description]
    """

    def __init__(self, *args, **kwargs):
        """Init method."""
        if "session_options" not in kwargs:
            kwargs["session_options"] = {}
        kwargs["session_options"]["autocommit"] = False
        # Configure Constraint Naming Conventions:
        # http://docs.sqlalchemy.org/en/latest/core/constraints.html
        # #constraint-naming-conventions
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
        super().__init__(*args, **kwargs)

    def init_app(self, app):
        """
        Call to init extension.

        Args:
            app ([type]): [description]
        """
        super().init_app(app)

        database_uri = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_uri or database_uri == "sqlite:///:memory:":
            raise Exception("SQLALCHEMY_DATABASE_URI must be configured!")
        # assert database_uri, "SQLALCHEMY_DATABASE_URI must be configured!"
        if database_uri.startswith("sqlite:"):
            self.event.listens_for(sqlalchemy.engine.Engine, "connect")(
                set_sqlite_pragma
            )

        app.extensions["migrate"] = AlembicDatabaseMigrationConfig(
            self, compare_type=True
        )

    def get_db_items(
            self,
            sql_alchemy_model,
            dict_schema,
            ma_schema,
            query_dict):
        """
        Return resource based on the passed models and query parameter.

        Args:
            sql_alchemy_model ([type]): SQLAlchemy ORM model
            dict_schema ([type]): dict with flask fields
            ma_schema ([type]): marshmallows schema
            query_dict (dict): query parameters

        Returns:
            dict: {"data": {"total": int, "rows": list},
                    "message" : str,
                    "error": str
                    }
        """
        if "offset" in query_dict.keys():
            offset = query_dict.get("offset")
        else:
            offset = 0
        if "limit" in query_dict.keys():
            limit = query_dict.get("limit")
        else:
            limit = current_app.config.get("PAGINATION_ITEMS_LIMIT")

        msg = None
        schema_keys = {}
        multiple_value_query_dict = {}

        for key in query_dict.keys():
            if key in dict_schema.keys():
                if isinstance(query_dict[key], (list, tuple)):
                    multiple_value_query_dict[key] = query_dict[key]
                else:
                    schema_keys[key] = query_dict.get(key)
        query = sql_alchemy_model.query

        # Filter items based on schema keys with one value
        if schema_keys:
            try:
                query = query.filter_by(**schema_keys)
            except sqlalchemy.exc.InvalidRequestError as ex:
                current_app.logger.error(ex)
                msg = "Unable to filter items based on query items (%s)" % str(
                    ex)

        # Filter items based on  schema keys with multiple values
        if multiple_value_query_dict:
            for key, value in multiple_value_query_dict.items():
                attr = getattr(sql_alchemy_model, key)
                try:
                    query = query.filter(attr.in_(value))
                except sqlalchemy.exc.InvalidRequestError as ex:
                    current_app.logger.error(ex)
                    msg = "Unable to filter items based on query items (%s)" % str(
                        ex)

        total = query.count()

        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)

        items = ma_schema.dump(query, many=True)[0]
        return create_response_item(msg, total, items)

    def get_db_item(self, sql_alchemy_model, ma_schema, query_dict):
        """
        Return data base item by its Id.

        Args:
            item_id (int):

        Returns:
            dict: info dict
        """
        db_item = sql_alchemy_model.query.filter_by(**query_dict).first_or_404(
            description="There is no data with item id %s" % str(query_dict)
        )
        # db_item = sql_alchemy_model.query.filter_by(**item_id_dict).first()
        db_item_json = ma_schema.dump(db_item)[0]

        return db_item_json

    def get_db_items_by_view(
        self, sql_alchemy_model, dict_schema, ma_schema, query_dict
    ):
        """Get db items by view."""
        msg = None
        schema_keys = {}
        multiple_value_query_dict = {}

        for key in query_dict.keys():
            if key in dict_schema.keys():
                if isinstance(query_dict[key], (list, tuple)):
                    multiple_value_query_dict[key] = query_dict[key]
                else:
                    schema_keys[key] = query_dict.get(key)

        query = self.session.query(sql_alchemy_model)

        total = query.count()

        items = ma_schema.dump(query, many=True)[0]

        return create_response_item(msg, total, items)

    def add_db_item(self, sql_alchemy_model, ma_schema, data):
        """
        Add item to db.

        Args:
            sql_alchemy_model ([type]): [description]
            data (dict): [description]

        Returns:
            SQLAlchemy db item: [description]
        """
        try:
            db_item = sql_alchemy_model(**data)
            self.session.add(db_item)
            self.session.commit()
            json_data = ma_schema.dump(db_item)[0]
            return json_data, HTTPStatus.OK
        except TypeError as ex:
            self.session.rollback()
            current_app.logger.error(ex)
            abort(HTTPStatus.NOT_ACCEPTABLE,
                  "Unable to add db item (%s)" % str(ex))
        except sqlalchemy.exc.DataError as ex:
            self.session.rollback()
            current_app.logger.error(ex)
            abort(HTTPStatus.NOT_ACCEPTABLE,
                  "Unable to add db item (%s)" % str(ex))
        except Exception as ex:
            self.session.rollback()
            current_app.logger.error(ex)
            abort(HTTPStatus.NOT_ACCEPTABLE,
                  "Unable to add db item (%s)" % str(ex))

    def update_db_item(
        self, sql_alchemy_model, ma_schema, item_id_dict, item_update_dict
    ):
        """
        Update item in db.

        Args:
            sql_alchemy_model ([type]): [description]
            item_id_dict ([type]): [description]
            item_update_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        result = None
        db_item = sql_alchemy_model.query.filter_by(
            **item_id_dict).first_or_404(
            description="There is no data with item id %s" %
            str(item_id_dict))
        if db_item:
            for key, value in item_update_dict.items():
                if hasattr(db_item, key):
                    setattr(db_item, key, value)
                else:
                    current_app.logger.error("Attribute %s not defined in the item model" % key)
            self.session.commit()
            result = ma_schema.dump(db_item)[0]
        return result

    def patch_db_item(
            self,
            sql_alchemy_model,
            ma_schema,
            item_id_dict,
            item_data_dict):
        """
        Patch db item.

        Args:
            sql_alchemy_model ([type]): [description]
            ma_schema : Marshmallows schema
            item_id_dict ([type]): [description]
            item_data_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        result = None
        db_item = sql_alchemy_model.query.filter_by(
            **item_id_dict).first_or_404(
            description="There is no data with item id %s" %
            str(item_id_dict))
        if db_item:
            for key, value in item_data_dict.items():
                if hasattr(db_item, key):
                    setattr(db_item, key, value)
                else:
                    abort(
                        HTTPStatus.NOT_ACCEPTABLE,
                        "Attribute %s not defined in the item model" % key,
                    )
            self.session.commit()
            result = ma_schema.dump(db_item)[0]

        return result

    def delete_db_item(self, sql_alchemy_model, item_id_dict):
        """
        Delete db item.

        Args:
            sql_alchemy_model ([type]): [description]
            item_id_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        db_item = sql_alchemy_model.query.filter_by(
            **item_id_dict).first_or_404(
            description="There is no data with item id %s" %
            str(item_id_dict))

        try:
            self.session.delete(db_item)
            self.session.commit()
            return True
        except Exception as ex:
            current_app.logger.error(ex)
            # log.exception(str(ex))
            self.session.rollback()
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(ex))
