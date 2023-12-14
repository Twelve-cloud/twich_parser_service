"""
twich_schemas.py: File, containing schemas related to twich parsing.
"""


from typing import Optional, Annotated
from datetime import datetime
from pydantic import Field, ValidationError, field_validator
from fields.twich_fields import TwichUserType, TwichStreamStatusType, TwichUserBroadcasterType
from schemas.base_schemas import BaseROSchema


class TwichGameSchema(BaseROSchema):
    """
    TwichGameSchema: Validation schema for Twich games.

    Args:
        BaseROSchema (_type_): Base superclass for TwichGameSchema.
    """

    id: Annotated[str, Field(min_length=1, max_length=128)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]


class TwichUserSchema(BaseROSchema):
    """
    TwichUserSchema: Validation schema for Twich users.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamSchema.
    """

    id: Annotated[str, Field(min_length=1, max_length=128)]
    login: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    display_name: Annotated[str, Field(min_length=0, max_length=128)]

    type: Annotated[TwichUserType, Field()]
    broadcaster_type: Annotated[TwichUserBroadcasterType, Field()]

    profile_image_url: Annotated[str, Field(min_length=0, max_length=256)]
    offline_image_url: Annotated[str, Field(min_length=0, max_length=256)]

    created_at: Annotated[datetime, Field()]

    @field_validator('created_at', mode='before')
    @classmethod
    def validate_created_at(cls, raw_created: str) -> datetime:
        """
        validate_created_at: Validate created date for being in range.

        Args:
            raw_created (str): Raw created date of the stream.

        Raises:
            ValidationError: Raised if created date is not vald.

        Returns:
            datetime: Validated created date.
        """

        created: datetime = datetime.strptime(raw_created, '%Y-%m-%dT%H:%M:%SZ')

        if not datetime(year=2000, month=1, day=1) <= created < datetime(year=2030, month=1, day=1):
            raise ValidationError('Create date must be in range')

        return created


class TwichStreamSchema(BaseROSchema):
    """
    TwichStreamSchema: Validation schema for Twich streams.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamSchema.
    """

    id: Annotated[str, Field(min_length=1, max_length=128)]

    user_id: Annotated[str, Field(min_length=1, max_length=128)]
    user_name: Annotated[str, Field(min_length=1, max_length=128)]
    user_login: Annotated[str, Field(min_length=1, max_length=128)]

    game_id: Annotated[str, Field(min_length=1, max_length=128)]
    game_name: Annotated[str, Field(min_length=1, max_length=128)]

    language: Annotated[str, Field(min_length=0, max_length=128)]
    title: Annotated[Optional[str], Field(min_length=0, max_length=128)]

    tags: Annotated[list[str], Field()]
    started_at: Annotated[datetime, Field()]
    viewer_count: Annotated[int, Field(ge=0)]
    type: Annotated[TwichStreamStatusType, Field()]

    @field_validator('started_at', mode='before')
    @classmethod
    def validate_started_at(cls, raw_started: str) -> datetime:
        """
        validate_started_at: Validate started date for being in range.

        Args:
            raw_started (str): Raw started date of the stream.

        Raises:
            ValidationError: Raised if started date is not vald.

        Returns:
            datetime: Validated started date.
        """

        started: datetime = datetime.strptime(raw_started, '%Y-%m-%dT%H:%M:%SZ')

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
