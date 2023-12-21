"""
game_schema.py: File, containing twich game schema.TwichGameReadSchema
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.schemas.base.base_schema import BaseROSchema


class TwichGameCreateSchema(BaseROSchema):
    """
    TwichGameCreateSchema: Validation create schema for Twich games.

    Args:
        BaseROSchema (_type_): Base superclass for TwichGameCreateSchema.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]


class TwichGameReadSchema(BaseROSchema):
    """
    TwichGameReadSchema: Validation read schema for Twich games.

    Args:
        BaseROSchema (_type_): Base superclass for TwichGameReadSchema.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]
    parsed_at: Annotated[datetime, Field()]
