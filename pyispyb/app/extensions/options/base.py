from datetime import datetime
import json

from starlette.types import ASGIApp

from ispyb import models

from ...globals import g
from ..database.middleware import db
from ..database.session import get_session
from ..database.utils import Paged, page
from .schema import Options, UIOptions


def setup_options(app: ASGIApp):
    """Add the db_options to the current app global"""
    with get_session() as session:
        app.db_options = get_options(get_all=True, session=session)


def get_options(get_all: bool = False, session=None) -> Options:
    if not session:
        session = db.session

    adminVars: list[models.AdminVar] = (session.query(models.AdminVar)).all()

    options = {}
    for adminVar in adminVars:
        try:
            # To support more complex data types `value` is currently varchar(1000)
            options[adminVar.name] = json.loads(adminVar.value)
        except json.decoder.JSONDecodeError:
            options[adminVar.name] = adminVar.value

    return Options(**options) if get_all else UIOptions(**options)


def update_options(options: Options) -> Options:
    options_dict = options.dict()
    current_options_dict = get_options(get_all=True).dict()

    for option_key, option_value in options_dict.items():
        if current_options_dict[option_key] == option_value:
            continue

        adminVar = (
            db.session.query(models.AdminVar)
            .filter(models.AdminVar.name == option_key)
            .first()
        )
        if adminVar:
            adminVar.value = json.dumps(option_value)
        else:
            adminVar = models.AdminVar(name=option_key, value=option_value)
            db.session.add(adminVar)

        db.session.commit()

        # Log changes in db_options
        adminActivity = models.AdminActivity(
            username=g.username,
            action="db_options",
            comments=f"changed `{option_key}` to `{option_value}`",
            dateTime=datetime.now(),
        )
        db.session.add(adminActivity)

        db.session.commit()

    return options


def get_activity(
    skip: int,
    limit: int,
) -> Paged[models.AdminActivity]:
    """Get admin activity"""
    query = db.session.query(models.AdminActivity).order_by(
        models.AdminActivity.dateTime.desc()
    )

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)
