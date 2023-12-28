"""
stream_schema.py: File, containing twich stream schema.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.schemas.base.base_schema import BaseROSchema
from application.schemas.fields.twich.stream_fields import TwichStreamStatusType


class TwichStreamSchema(BaseROSchema):
    """
    TwichStreamSchema: Validation read schema for Twich streams.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamSchema.
    """

    id: Annotated[int, Field(ge=0)]

    user_id: Annotated[int, Field(ge=0)]
    user_name: Annotated[str, Field(min_length=1, max_length=128)]
    user_login: Annotated[str, Field(min_length=1, max_length=128)]

    game_id: Annotated[int, Field(ge=0)]
    game_name: Annotated[str, Field(min_length=1, max_length=128)]

    language: Annotated[str, Field(min_length=0, max_length=128)]
    title: Annotated[str, Field(min_length=0, max_length=128)]

    tags: Annotated[list[str], Field()]
    started_at: Annotated[datetime, Field()]
    viewer_count: Annotated[int, Field(ge=0)]
    type: Annotated[TwichStreamStatusType, Field()]
    parsed_at: Annotated[datetime, Field()]
