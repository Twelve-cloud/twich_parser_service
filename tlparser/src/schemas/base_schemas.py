"""
base_schemas.py: File, containing base schemas for entire application.
"""


from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class BaseROSchema(BaseModel):
    """
    BaseROSchema: Parent schema for every read-only schemas.

    Args:
        BaseModel (_type_): Base superclass for BaseROSchema.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(strict=True, frozen=True, extra='forbid')
