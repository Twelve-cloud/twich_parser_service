"""
lamoda_schemas.py: File, containing schemas related to lamoda parsing.
"""


from typing import Annotated
from pydantic import Field
from schemas.base_schemas import BaseROSchema


class LamodaProductSchema(BaseROSchema):
    """
    LamodaProductSchema: Validation schema for Lamoda products.

    Args:
        BaseROSchema (_type_): Base superclass for LamodaProductSchema.
    """

    category: Annotated[str, Field(min_length=1)]
    vendor: Annotated[str, Field(min_length=1)]
    url: Annotated[str, Field(min_length=1)]
    price: Annotated[int, Field(gt=0)]
    attributes: Annotated[list[dict], Field()]
