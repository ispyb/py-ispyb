from typing import Optional

from fastapi import Depends

from ispyb import models

from ....dependencies import pagination, permission
from ....app.extensions.database.utils import Paged
from ....core.schemas.utils import paginated
from ...modules.admin import activity as crud
from ...schemas.admin.activity import AdminActivity, ActionType
from .base import router


@router.get(
    "/activity",
    response_model=paginated(AdminActivity),
)
def get_activity(
    page: dict[str, int] = Depends(pagination),
    action_type: Optional[ActionType] = None,
    depends=Depends(permission("view_activity")),
) -> Paged[models.AdminActivity]:
    """Get list of admin activity"""
    return crud.get_activity(action_type=action_type, **page)
