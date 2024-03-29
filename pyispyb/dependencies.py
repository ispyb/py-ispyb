import enum
import logging
from typing import Callable, Optional, Any

from fastapi import HTTPException, Query
from pydantic import conint

from .app.globals import g


logger = logging.getLogger(__name__)


class Order(str, enum.Enum):
    asc = "asc"
    desc = "desc"


def pagination(
    skip: Optional[conint(ge=0)] = Query(0, description="Results to skip"),
    limit: Optional[conint(gt=0)] = Query(25, description="Number of results to show"),
) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


def order_by_factory(columns: dict[str], enumName: str) -> Callable:
    order_by_enum = enum.Enum(enumName, {k: k for k in columns.keys()})

    def order_by(
        order_by: Optional[order_by_enum] = Query(
            None, description="Field to order by"
        ),
        order: Optional[Order] = Query(None, description="Order direction"),
    ) -> dict[str, Any]:
        order_fields = {"order_by": order_by}
        order_fields["order"] = order

        return order_fields

    return order_by


def filter(filter: str) -> str:
    return filter


def permission(permission: str):
    """Requires the user to have the specified permission"""

    async def with_permission() -> bool:
        if permission not in g.permissions:
            logger.info(
                f"User {g.login} tried to access route with required permission {permission}"
            )
            raise HTTPException(
                status_code=403,
                detail="Not Authorized",
            )

        return True

    return with_permission


def has_permission(permission: str):
    return permission in g.permissions
