import datetime
from typing import Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from ispyb import models


class SessionResponse(sqlalchemy_to_pydantic(models.BLSession)):
    lastUpdate: Optional[datetime.datetime]

    BeamLineSetup: Optional[sqlalchemy_to_pydantic(models.BeamLineSetup)]
