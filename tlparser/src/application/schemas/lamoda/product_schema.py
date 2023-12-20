"""
product_schema.py: File, containing lamoda product schema.
"""


from datetime import datetime
from typing import Annotated
from application.fields.lamoda.product_fields import CurrencyType
from application.schemas.base.base_schema import BaseROSchema
from pydantic import Field, ValidationError, field_validator


class LamodaProductCreateSchema(BaseROSchema):
    """
    LamodaProductCreateSchema: Validation create schema for Lamoda products.

    Args:
        BaseROSchema (_type_): Base superclass for LamodaProductCreateSchema.
    """

    sku: Annotated[str, Field(min_length=1, max_length=128)]
    url: Annotated[str, Field(min_length=1, max_length=256)]
    category: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    price: Annotated[float, Field(ge=0)]
    price_currency: Annotated[CurrencyType, Field()]
    price_valid_until: Annotated[datetime, Field()]

    @field_validator('price_valid_until', mode='before')
    @classmethod
    def validate_created_at(cls, raw_until: str) -> datetime:
        """
        validate_created_at: Validate date until price is valid.

        Args:
            raw_until (str): Raw date until price is valid.

        Raises:
            ValidationError: Raised if created date is not vald.

        Returns:
            datetime: Validated date until price is valid.
        """

        until: datetime = datetime.strptime(raw_until[:-3], '%Y-%m-%d %H:%M:%S.%f')

        if not datetime(year=2020, month=1, day=1) <= until < datetime(year=2030, month=1, day=1):
            raise ValidationError('Create date must be in range')

        return until


class LamodaProductReadSchema(BaseROSchema):
    """
    LamodaProductReadSchema: Validation read schema for Lamoda products.

    Args:
        BaseROSchema (_type_): Base superclass for LamodaProductReadSchema.
    """

    sku: Annotated[str, Field(min_length=1, max_length=128)]
    url: Annotated[str, Field(min_length=1, max_length=256)]
    category: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    price: Annotated[float, Field(ge=0)]
    price_currency: Annotated[CurrencyType, Field()]
    price_valid_until: Annotated[datetime, Field()]
    parsed_at: Annotated[datetime, Field()]
