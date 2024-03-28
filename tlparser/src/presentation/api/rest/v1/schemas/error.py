"""
error.py: File, containing error schema.
"""


from typing import Annotated, Optional
from pydantic import Field
from presentation.api.rest.v1.schemas.base import Schema


class JSONAPIErrorSchema(Schema):
    id: Annotated[int, Field(description='ID of the error.')]
    status: Annotated[str, Field(description='Status of the error.')]
    code: Annotated[int, Field(description='Code of the error.')]
    links: Annotated[Optional[dict], Field(default=None, description='Links.')]
