"""
twich_schemas.py: File, containing schemas related to twich parsing.
"""


from typing import Optional, Annotated
from datetime import datetime
from pydantic import Field, ValidationError, field_validator
from schemas.base_schemas import BaseROSchema


class TwichGameSchema(BaseROSchema):
    """
    TwichGameSchema: Validation schema for Twich games.

    Args:
        BaseROSchema (_type_): Base superclass for TwichGameSchema.
    """

    game_id: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    viewers: Annotated[int, Field(ge=0)]
    followers: Annotated[int, Field(ge=0)]
    labels: Annotated[list[str], Field()]

    @field_validator('labels')
    @classmethod
    def validate_labels(cls, labels: list[str]) -> list[str]:
        """
        validate_labels: Validate label for being non-empty.

        Args:
            labels (list[str]): Game label.

        Raises:
            ValidationError: Raised if any of labels are empty.

        Returns:
            list[str]: Validated labels.
        """

        if not all(labels):
            raise ValidationError('label must not be empty')

        return labels


class TwichUserSchema(BaseROSchema):
    """
    TwichUserSchema: Validation schema for Twich users.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamSchema.
    """

    user_id: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    followers: Annotated[int, Field(ge=0)]
    is_live: Annotated[bool, Field()]


class TwichStreamSchema(BaseROSchema):
    """
    TwichStreamSchema: Validation schema for Twich streams.

    Args:
        BaseROSchema (_type_): Base superclass for TwichStreamSchema.
    """

    user_id: Annotated[str, Field(min_length=1)]
    viewers: Annotated[int, Field(ge=0)]
    started_at: Annotated[datetime, Field()]

    @field_validator('started_at')
    @classmethod
    def validate_started_at(cls, started: Optional[datetime]) -> Optional[datetime]:
        """
        validate_started_at: Validate started date for being in range.

        Args:
            started (datetime): Started date of the stream or None.

        Raises:
            ValidationError: Raised if started date is not vald.

        Returns:
            datetime: Validated started date or None.
        """

        if started is None:
            return started

        if datetime(year=2020, month=1, day=1) <= started < datetime(year=2030, month=1, day=1):
            raise ValidationError('Start date must be in range')

        return started
