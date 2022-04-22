import enum
from typing import Optional, Any

from fastapi import Query


class Order(str, enum.Enum):
    asc = "asc"
    desc = "desc"


def pagination(
    skip: Optional[int] = Query(0, description="Results to skip"),
    limit: Optional[int] = Query(25, description="Number of results to show"),
) -> dict[str, int]:
    assert skip is not None
    assert limit is not None

    return {"skip": skip, "limit": limit}


def order_by(
    order_by: Optional[str] = Query(None, description="Field to order by"),
    order: Optional[Order] = Query("asc", description="Order direction"),
) -> dict[str, Any]:
    assert order_by is not None
    order_fields = {"order_by": order_by}

    if order:
        order_fields["order"] = order

    return order_fields


def filter_dep(filter_dep: str) -> str:
    return filter_dep
