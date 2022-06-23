from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models


class SSXDataCollectionResponse(
    sqlalchemy_to_pydantic(models.SSXDataCollection, exclude=["dataCollectionId"])
):
    DataCollection: sqlalchemy_to_pydantic(
        models.DataCollection, exclude=["dataCollectionId"]  # noqa: F821 flake8 bug
    )


class SSXSampleCreate(
    sqlalchemy_to_pydantic(models.SSXSample, exclude=["ssxSampleId", "ssxBufferId"])
):
    buffer: sqlalchemy_to_pydantic(
        models.SSXBuffer, exclude=["ssxBufferId"]  # noqa: F821 flake8 bug
    )


class DataCollectionCreate(
    sqlalchemy_to_pydantic(models.DataCollection, exclude=["dataCollectionId"])
):
    pass


class SSXDataCollectionCreate(
    DataCollectionCreate,
    sqlalchemy_to_pydantic(
        models.SSXDataCollection,
        exclude=["ssxSampleId", "ssxDataCollectionId", "dataCollectionId"],
    ),
):
    sample: SSXSampleCreate
