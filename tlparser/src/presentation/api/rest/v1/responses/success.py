"""
success.py: File, containing success response schema.
"""


from typing import Annotated, Optional, Sequence
from pydantic import Field
from presentation.api.rest.v1.responses.base import ResponseSchema
from presentation.api.rest.v1.schemas import JSONAPIObjectSchema


class JSONAPISuccessResponseSchema(ResponseSchema):
    data: Annotated[Sequence[JSONAPIObjectSchema], Field(description='List of objects.')]
    meta: Annotated[Optional[dict], Field(default=None, description='JSON-API metadata.')]
    jsonapi: Annotated[Optional[float], Field(default=1.1, description='JSON-API version.')]
