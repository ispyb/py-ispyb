from pydantic import BaseModel, Field


class BeamLineGroupBeamLine(BaseModel):
    beamLineName: str = Field(title="Beamline Name")
    archived: bool = Field(
        False, title="Archived", description="Whether this beamline is archived"
    )


class BeamLineGroup(BaseModel):
    groupName: str = Field(title="Group Name")
    uiGroup: str = Field(title="UI Group")
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
    beamLineGroups: list[BeamLineGroup] = Field([], title="Beamline Groups")
