"""
stream_schema.py: File, containing twich stream schema.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field, ValidationError, field_validator
from presentation.schemas.base.base_schema import BaseROSchema
from presentation.schemas.fields.twich.stream_fields import TwichStreamStatusType


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

    @field_validator('started_at')
    @classmethod
    def validate_started_at(cls, started: datetime) -> datetime:
        """
        validate_started_at: Validate started date for being in range.

        Args:
            started (datetime): Started date of the stream.

        Raises:
            ValidationError: Raised if started date is not vald.

        Returns:
            datetime: Validated started date.
        """

        if not datetime(year=2000, month=1, day=1) <= started < datetime(year=2030, month=1, day=1):
            raise ValidationError('Start date must be in range')

        return started

    @field_validator('tags')
    @classmethod
    def validate_tags(cls, tags: list[str]) -> list[str]:
        """
        validate_tags: Validate tags for being in range.

        Args:
            tags (list[str]): List of tags.

        Raises:
            ValidationError: Raised if tag length is not in range.

        Returns:
            list[str]: Validated list of tags.
        """

        if list(filter(lambda tag: 1 > len(tag) or len(tag) > 128, tags)):
            raise ValidationError('tag length must be in range 1...128')

        return tags
