from typing import Optional

from pydantic import BaseModel


class RobotAction(BaseModel):
    actionType: str
    status: Optional[str]
    message: Optional[str]

    class Config:
        orm_mode = True
