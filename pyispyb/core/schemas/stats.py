from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field


class BreakdownOverviewCounts(BaseModel):
    datacollections: int
    failed: int
    datacollectionTypes: dict[str, int]
    robot: int
    edge: int
    xrf: int


class BreakdownOverviewSession(BaseModel):
    startDate: datetime
    endDate: datetime
    duration: float
    beamLineName: str
    session: Optional[str]
    counts: BreakdownOverviewCounts


class BreakdownOverviewRun(BaseModel):
    startDate: datetime
    endDate: datetime
    duration: float
    run: str
    counts: BreakdownOverviewCounts


class BreakdownPoint(BaseModel):
    eventType: str
    startTime: datetime
    endTime: datetime

    protein: Optional[str]
    sample: Optional[str]

    subType: Optional[str]
    status: Optional[str]

    title: Optional[str]
    session: Optional[str]


class BreakdownPlottable(BaseModel):
    title: str
    unit: Optional[str]
    data: list


class BreakdownPlottables(BaseModel):
    time: list[datetime]
    series: list[BreakdownPlottable]


class Breakdown(BaseModel):
    overview: Union[BreakdownOverviewSession, BreakdownOverviewRun]
    history: list[BreakdownPoint]
    plottables: BreakdownPlottables


class TimeEntry(BaseModel):
    duration: float = Field(0, title="Total time")
    startup: float = Field(0, title="Time before first data collection")
    datacollection: float = Field(0, title="Time used for data collections")
    edge: float = Field(0, title="Time used for energy scans")
    xrf: float = Field(0, title="Total used for xrf scans")
    robot: float = Field(0, title="Total used for robot / sample actions")
    strategy: float = Field(0, title="Time waiting for strategy")
    centring: float = Field(0, title="Total waiting for centring")
    fault: float = Field(0, title="Time taken with faults")
    remaining: float = Field(0, title="Time remaining")
    thinking: float = Field(0, title="Time not used by other types")

    def calc_thinking(self) -> float:
        return (
            self.duration
            - self.startup
            - self.datacollection
            - self.edge
            - self.xrf
            - self.robot
            - self.strategy
            - self.centring
            - self.fault
        )


class AverageTimeEntry(TimeEntry):
    count: int = 0

    def average(self, *models: TimeEntry):
        for field in TimeEntry.__fields__.keys():
            if len(models) > 0:
                setattr(
                    self,
                    field,
                    sum([getattr(model, field) for model in models]) / len(models),
                )


class SessionTimeEntry(TimeEntry):
    session: str = Field(title="The session")


class Times(BaseModel):
    average: TimeEntry = Field(title="The average times")
    sessions: list[SessionTimeEntry] = Field(title="Times per session")


class Hourly(BaseModel):
    hour: list[int]
    average: list[float]


class Hourlies(BaseModel):
    datacollections: Hourly
    loaded: Hourly


class ExperimentTypeMessages(BaseModel):
    count: int = Field(title="Frequency of this error message")
    message: str = Field(title="The error message")


class ExperimentTypeGroup(BaseModel):
    experimentType: str = Field(title="Experiment type")
    total: int = Field(title="Total data collections")
    failed: int = Field(title="Failed data collections")
    failedPercent: float = 0
    aborted: int = Field(title="Aborted data collections")
    abortedPercent: float = 0
    messages: list[ExperimentTypeMessages] = Field(title="Error Messages")


class ExperimentTypeGroupPrepare(ExperimentTypeGroup):
    """Used to prepare the Error data"""

    messages: dict[str, ExperimentTypeMessages]


class Errors(BaseModel):
    totals: list[ExperimentTypeGroup]


class ParameterHistogram(BaseModel):
    beamLineName: str
    bin: list[int]
    frequency: list[int]


class ParameterHistograms(BaseModel):
    parameter: str
    unit: str
    beamLines: list[ParameterHistogram]


class VRun(BaseModel):
    run: str
    runId: int
    startDate: datetime
    endDate: datetime

    class Config:
        orm_mode = True
