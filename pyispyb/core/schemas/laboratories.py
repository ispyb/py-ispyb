from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from ispyb import models
from pyispyb.core.schemas.validators import WordDashSpace


PydanticLaboratoryCreate = sqlalchemy_to_pydantic(
    models.Laboratory, exclude={"laboratoryId", "recordTimeStamp"}
)

PydanticLaboratory = sqlalchemy_to_pydantic(models.Laboratory)


class LaboratoryCreate(PydanticLaboratoryCreate):

    # name, city and country required to be able to check for existing Laboratory in DB (to update or create)
    # Optionally the system will check also against laboratoryExtPk (User Portal Sync)
    name: str = WordDashSpace(title="Laboratory Name")
    address: str
    city: str
    country: str


class Laboratory(PydanticLaboratory):
    laboratoryId: int

    class Config:
        orm_mode = True
