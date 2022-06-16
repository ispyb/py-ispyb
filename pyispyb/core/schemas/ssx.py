from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models


class SSXDataCollectionResponse(
    sqlalchemy_to_pydantic(models.SSXDataCollection, exclude=["dataCollectionId"])
):
    DataCollection: sqlalchemy_to_pydantic(
        models.DataCollection, exclude=["dataCollectionId"]
    )


class SSXDataCollectionCreate(
    sqlalchemy_to_pydantic(models.SSXDataCollection, exclude=["dataCollectionId"])
):
    DataCollection: sqlalchemy_to_pydantic(
        models.DataCollection, exclude=["dataCollectionId"]
    )
