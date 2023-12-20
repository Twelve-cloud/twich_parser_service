"""
base_schema.py: File, containing base schema for entire application.
"""


from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class BaseROSchema(BaseModel):
    """
    BaseROSchema: Parent schema for every read-only schemas.

    Args:
        BaseModel (_type_): Base superclass for BaseROSchema.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(strict=False, frozen=True, extra='ignore')
