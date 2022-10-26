from typing import Optional

from pydantic import BaseModel, Field


class BeamLineGroupBeamLine(BaseModel):
    beamLineName: str = Field(title="Beamline Name")
    sampleChangerType: Optional[str] = Field(
        None, title="Sample Changer Type", nullable=True
    )
    sampleChangerCapacity: Optional[int] = Field(
        None,
        title="Sample Changer Capacity",
        description="If no specific type is available a capacity can be defined for the generic view",
        nullable=True,
    )
    archived: bool = Field(
        False,
        title="Archived",
        description="Whether this beamline is archived (no longer displayed on landing page)",
    )


class BeamLineGroup(BaseModel):
    groupName: str = Field(title="Group Name", descriptiopn="A group of beamlines")
    uiGroup: str = Field(title="UI Group", description="Display type to use in the UI")
    permission: str = Field(
        title="Permission",
        description="Permission required to view all proposals from these beamlines",
    )
    beamLines: list[BeamLineGroupBeamLine] = Field([], title="Beamlines")


class UIOptions(BaseModel):
    """Publicly available UI options"""

    motd: str = Field(
        "", title="Message of the Day", description="Displayed at the top of the UI"
    )
    beamLineGroups: list[BeamLineGroup] = Field([], title="Beamline Groups")


class Options(UIOptions):
    """All available application options"""

    query_debug: bool = Field(
        False, title="Query Debugging", description="Enable query debugging"
    )
    enable_legacy_routes: bool = Field(
        True, title="Legacy Routes", description="Enable legacy routes"
    )
    enable_webservice_routes: bool = Field(
        True,
        title="Webservice Routes",
        description="Enable webservices called from external applications",
    )
    create_person_on_missing: bool = Field(
        False,
        title="Create Missing Login",
        description="Automatically create a `Person` entry if the `login` is missing from the database. (!) Warning modifies the database",
    )
