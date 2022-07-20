<<<<<<< HEAD
=======
import enum
>>>>>>> activity is also used to store `whos online` information, move to more generic location
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
<<<<<<< HEAD
    depends=Depends(permission("view_activity")),
=======
    depends=Depends(permission("admin_activity")),
>>>>>>> activity is also used to store `whos online` information, move to more generic location
) -> Paged[models.AdminActivity]:
    """Get list of admin activity"""
    return crud.get_activity(action_type=action_type, **page)
