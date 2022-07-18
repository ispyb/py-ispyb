import os
import time
import logging
from typing import Optional, Generic, TypeVar, Any

from pydantic import BaseModel
import sqlalchemy.engine
import sqlalchemy.engine.interfaces
import sqlalchemy.event
import sqlalchemy.orm
import sqlparse


logger = logging.getLogger("db")


def order(
    query: "sqlalchemy.orm.Query[Any]",
    sort_map: dict[str, "sqlalchemy.Column[Any]"],
    order: str,
    default: Optional[list[str]] = None,
    order_by: Optional[str] = None,
) -> "sqlalchemy.orm.Query[Any]":
    """Sort a result set by a field

    Args:
        query (sqlalchemy.query): The current query
        sort_map (dict): A mapping of field(str) -> sqlalchemy.Column

    Kwargs:
        order_by (str): Field to sort by
        order (Order): Asc or desc

    Returns
        query (sqlalchemy.orm.Query): The ordered query
    """
    if not (order_by and order) and not default:
        return query

    if default:
        order_by = default[0]
        order = default[1]

    if order_by not in sort_map:
        logger.warning(f"Unknown order_by {order_by}")
        return query

    return query.order_by(getattr(sort_map[order_by], str(order))())


def page(
    query: "sqlalchemy.orm.Query[Any]", skip: int, limit: int
) -> "sqlalchemy.orm.Query[Any]":
    """Paginate a `Query`

    Kwargs:
        per_page (str): Number of rows per page
        page (str): Page number to display

    Returns
        query (sqlalchemy.orm.Query): The paginated query
    """
    return query.limit(limit).offset(skip)


T = TypeVar("T")


class Paged(BaseModel, Generic[T]):
    """Page a model result set"""

    total: int
    results: list[T]
    skip: Optional[int]
    limit: Optional[int]

    @property
    def first(self) -> T:
        return self.results[0]


def pretty(query: "sqlalchemy.orm.Query[Any]", show: bool = False) -> str:
    """Pretty print a `Query`"""
    text: str = sqlparse.format(str(query), reindent=True, keyword_case="upper")
    if show:
        print(text)

    return text


def with_metadata(
    results: list[sqlalchemy.engine.row.Row], metadata: list[str]
) -> list[sqlalchemy.engine.row.Row]:
    """Add metadata to rows base _metadata attribute"""
    parsed = []
    for result in results:
        for meta_id, meta_value in enumerate(result[1:]):
            result[0]._metadata[metadata[meta_id]] = meta_value
        parsed.append(result[0])

    return parsed


class CustomBase:
    @property
    def _metadata(self) -> dict[str, Any]:
        if not hasattr(self, "_additional_metadata"):
            self._additional_metadata: dict[str, Any] = {}
        return self._additional_metadata


ENABLE_DEBUG_LOGGING = False


def enable_debug_logging() -> None:
    global ENABLE_DEBUG_LOGGING
    """Write debug level logging output for every executed SQL query.
    This setting will persist throughout the Python process lifetime and affect
    all existing and future sqlalchemy sessions. This should not be used in
    production as it can be expensive, can leak sensitive information, and,
    once enabled, cannot be disabled.
    """
    if ENABLE_DEBUG_LOGGING:
        return
    ENABLE_DEBUG_LOGGING = True

    _sqlalchemy_root = os.path.dirname(sqlalchemy.__file__)

    import traceback

    indent = "    "

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "before_cursor_execute")  # type: ignore
    def before_cursor_execute(
        conn: sqlalchemy.engine.Connection,
        cursor: "sqlalchemy.engine.interfaces.DBAPICursor",  # type: ignore
        statement: "sqlalchemy.orm.Query[Any]",
        parameters: tuple[Any],
        context: sqlalchemy.engine.ExecutionContext,
        executemany: bool,
    ) -> None:
        conn.info.setdefault("query_start_time", []).append(time.perf_counter())
        conn.info.setdefault("count", 0)
        conn.info["count"] += 1

        cause = ""
        for frame, line in traceback.walk_stack(None):
            if frame.f_code.co_filename.startswith(_sqlalchemy_root):
                continue
            cause = f"\n{indent}originating from {frame.f_code.co_filename}:{line}"
            break
        if parameters:
            str_parameters = f"\n{indent}with parameters={parameters}"
        else:
            str_parameters = ""

        logger.debug(
            f"SQL query #{conn.info['count']}:\n"
            + pretty(statement)
            + str_parameters
            + cause
        )

    @sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "after_cursor_execute")  # type: ignore
    def after_cursor_execute(
        conn: sqlalchemy.engine.Connection,
        cursor: "sqlalchemy.engine.interfaces.DBAPICursor",  # type: ignore
        statement: "sqlalchemy.orm.Query[Any]",
        parameters: tuple[Any],
        context: sqlalchemy.engine.ExecutionContext,
        executemany: bool,
    ) -> None:
        total = round(time.perf_counter() - conn.info["query_start_time"].pop(-1), 4)
        logger.debug(indent + f"SQL query #{conn.info['count']} took: {total} seconds")
