from fastapi import Depends, Request

from ispyb import models

from ...dependencies import pagination, permission
from ..extensions.database.utils import Paged
from ...core.schemas.utils import paginated
from ..base import AuthenticatedAPIRouter
from ..extensions.options import base as crud
from ..extensions.options.schema import AdminActivity, Options, UIOptions

router = AuthenticatedAPIRouter(prefix="/options", tags=["Options"])


@router.get(
    "/ui",
    response_model=UIOptions,
)
def get_ui_options() -> UIOptions:
    """Get the available UI database options"""
    return crud.get_options()


@router.get(
    "",
    response_model=Options,
)
def get_options(depends: bool = Depends(permission("admin_options"))) -> Options:
    """Get the available database options"""
    return crud.get_options(get_all=True)


@router.post(
    "",
    response_model=Options,
)
def update_options(
    options: Options, request: Request, depends=Depends(permission("admin_options"))
) -> Options:
    """Update the database options"""
    crud.update_options(options)
    options = crud.get_options(get_all=True)
    request.app.db_options = options
    return options


@router.get(
    "/activity",
    response_model=paginated(AdminActivity),
)
def get_activity(
    page: dict[str, int] = Depends(pagination),
    depends=Depends(permission("admin_options")),
) -> Paged[models.AdminActivity]:
    """Get list of admin activity"""
    return crud.get_activity(**page)
