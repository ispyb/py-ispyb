<<<<<<< HEAD
from pydantic import BaseModel, Field


=======
from datetime import datetime

from pydantic import BaseModel, Field


class AdminActivity(BaseModel):
    username: str
    action: str
    comments: str
    dateTime: datetime

    class Config:
        orm_mode = True


>>>>>>> add db options, add example for legacy routes
class UIOptions(BaseModel):
    """Publicly available UI options"""

    motd: str = Field(
        "", title="Message of the Day", description="Displayed at the top of the UI"
    )


class Options(UIOptions):
    """All available application options"""

    query_debug: bool = Field(
        False, title="Query Debugging", description="Enable query debugging"
    )
    enable_legacy_routes: bool = Field(
<<<<<<< HEAD
        True, title="Legacy Routes", description="Enable legacy routes"
=======
        False, title="Legacy Routes", description="Enable legacy routes"
>>>>>>> add db options, add example for legacy routes
    )
