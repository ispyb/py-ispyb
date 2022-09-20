import enum
from typing import Callable, Optional, Any

from fastapi import HTTPException, Query

from .app.globals import g


class Order(str, enum.Enum):
    asc = "asc"
    desc = "desc"


def pagination(
    skip: Optional[int] = Query(0, description="Results to skip"),
    limit: Optional[int] = Query(25, description="Number of results to show"),
) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


def order_by_factory(columns: dict[str], enumName: str) -> Callable:
    order_by_enum = enum.Enum(enumName, {k: k for k in columns.keys()})

    def order_by(
        order_by: Optional[order_by_enum] = Query(
            None, description="Field to order by"
        ),
        order: Optional[Order] = Query(Order.asc, description="Order direction"),
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
            raise HTTPException(status_code=403, detail="Not Authorised")

        return True

    return with_permission
