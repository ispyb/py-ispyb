from typing import Any
from pydantic import Field


def WordDash(*args: Any, **kwargs: Any) -> Any:
    return Field(*args, regex=r"^([\w-])+$", **kwargs)


def WordDashSpace(*args: Any, **kwargs: Any) -> Any:
    return Field(*args, regex=r"^([\w\s-])+$", **kwargs)


def WordDashSpaceNC(*args: Any, **kwargs: Any) -> Any:
    """Word, Space, New Line, Comma, Dash"""
    return Field(*args, regex=r"^([\w\s\n,-])+$", **kwargs)


def WordDashSpaceBC(*args: Any, **kwargs: Any) -> Any:
    """Word, Space, Brackets, Dash"""
    return Field(*args, regex=r"^([\w-\s\(\)\'])+$", **kwargs)
