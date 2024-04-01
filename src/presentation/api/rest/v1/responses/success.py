"""
success.py: File, containing success response schema.
"""


from typing import (
    Optional,
    Sequence,
)

from pydantic import Field

from presentation.api.rest.v1.responses.base import ResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIObjectSchema


class JSONAPISuccessResponseSchema(ResponseSchema):
    data: Sequence[JSONAPIObjectSchema] = Field(description='List of objects.')
    included: Optional[Sequence[JSONAPIObjectSchema]] = Field(default=None, description='Included.')
    meta: Optional[dict] = Field(default=None, description='JSON-API metadata.')
    jsonapi: Optional[float] = Field(default=1.1, description='JSON-API version.')
