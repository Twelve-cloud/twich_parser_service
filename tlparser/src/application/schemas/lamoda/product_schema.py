"""
product_schema.py: File, containing lamoda product schema.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.schemas.base.base_schema import BaseROSchema
from application.schemas.fields.lamoda.product_fields import CurrencyType


class LamodaProductSchema(BaseROSchema):
    """
    LamodaProductSchema: Validation read schema for Lamoda products.

    Args:
        BaseROSchema (_type_): Base superclass for LamodaProductSchema.
    """

    sku: Annotated[str, Field(min_length=1, max_length=128)]
    url: Annotated[str, Field(min_length=1, max_length=256)]
    category: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    price: Annotated[float, Field(ge=0)]
    price_currency: Annotated[CurrencyType, Field()]
    price_valid_until: Annotated[datetime, Field()]
    parsed_at: Annotated[datetime, Field()]
