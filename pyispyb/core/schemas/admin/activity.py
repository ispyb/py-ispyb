from datetime import datetime
import enum

from pydantic import BaseModel


class ActionType(str, enum.Enum):
    db_options = "db_options"
    online = "online"


class AdminActivity(BaseModel):
    username: str
    action: str
    comments: str
    dateTime: datetime

    class Config:
        orm_mode = True
