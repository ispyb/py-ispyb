from fastapi import Depends

from ...dependencies import permission
from ..base import AuthenticatedAPIRouter
from ..extensions.options import base as crud
from ..extensions.options.schema import Options, UIOptions

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
def get_options(depends: bool = Depends(permission("manage_options"))) -> Options:
    """Get the available database options"""
    return crud.get_options(get_all=True)


@router.patch(
    "",
    response_model=Options,
)
def update_options(
    options: Options, depends=Depends(permission("manage_options"))
) -> Options:
    """Update the database options"""
    from pyispyb.app.main import app

    crud.update_options(options)
    options = crud.get_options(get_all=True)
    app.db_options = options
    return options
