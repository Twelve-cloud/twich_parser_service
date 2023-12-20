"""
user_schema.py: File, containing twich user schema.
"""


from datetime import datetime
from typing import Annotated
from application.fields.twich.user_fields import TwichUserBroadcasterType, TwichUserType
from application.schemas.base.base_schema import BaseROSchema
from pydantic import Field, ValidationError, field_validator


class TwichUserCreateSchema(BaseROSchema):
    """
    TwichUserCreateSchema: Validation create schema for Twich users.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamCreateSchema.
    """

    id: Annotated[int, Field(ge=0)]
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


class TwichUserReadSchema(BaseROSchema):
    """
    TwichUserReadSchema: Validation read schema for Twich users.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamReadSchema.
    """

    id: Annotated[int, Field(ge=0)]
    login: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    display_name: Annotated[str, Field(min_length=0, max_length=128)]

    type: Annotated[TwichUserType, Field()]
    broadcaster_type: Annotated[TwichUserBroadcasterType, Field()]

    profile_image_url: Annotated[str, Field(min_length=0, max_length=256)]
    offline_image_url: Annotated[str, Field(min_length=0, max_length=256)]

    created_at: Annotated[datetime, Field()]
    parsed_at: Annotated[datetime, Field()]
