from typing import Optional

from pydantic import BaseModel, create_model
from pydantic.main import ModelMetaclass


def paginated(model: ModelMetaclass) -> ModelMetaclass:
    class PaginatedModel(BaseModel):
        total: int
        results: list[model]  # type: ignore
        skip: int
        limit: int

    cls_name = f"Paginated<{model.__name__}>"
    PaginatedModel.__name__ = cls_name
    PaginatedModel.__qualname__ = cls_name

    return PaginatedModel


def make_optional(baseclass):
    # https://stackoverflow.com/questions/67699451/make-every-fields-as-optional-with-pydantic
    fields = baseclass.__fields__
    validators = {"__validators__": baseclass.__validators__}
    optional_fields = {
        key: (Optional[item.type_], None) for key, item in fields.items()
    }
    return create_model(
        f"{baseclass.__name__}Optional", **optional_fields, __validators__=validators
    )
