from pydantic import BaseModel
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
