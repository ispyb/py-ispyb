from typing import Literal, Optional, Dict, Any
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from ispyb import models


class EventCreate(BaseModel):
    type: Literal["XrayDetection", "XrayExposure", "LaserExcitation", "ReactionTrigger"]
    name: Optional[str]
    offset: float
    duration: Optional[float]
    period: Optional[float]
    repetition: Optional[float]


class EventChainCreate(BaseModel):
    name: Optional[str]
    events: list[EventCreate]


class EventResponse(sqlalchemy_to_pydantic(models.Event)):
    EventType: sqlalchemy_to_pydantic(models.EventType)

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        kwargs.pop("exclude_none")
        return super().dict(*args, exclude_none=True, **kwargs)


class EventChainResponse(sqlalchemy_to_pydantic(models.EventChain)):
    events: list[EventResponse]

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        kwargs.pop("exclude_none")
        return super().dict(*args, exclude_none=True, **kwargs)
