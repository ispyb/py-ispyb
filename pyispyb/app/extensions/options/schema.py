from pydantic import BaseModel, Field


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
