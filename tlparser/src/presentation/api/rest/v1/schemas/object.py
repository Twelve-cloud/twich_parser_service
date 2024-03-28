"""
object.py: File, containing object schema.
"""


from typing import Annotated, Optional
from pydantic import Field
from presentation.api.rest.v1.schemas.base import Schema


class JSONAPIObjectSchema(Schema):
    id: Annotated[int, Field(description='ID of the object.')]
    type: Annotated[str, Field(description='Type of the object.')]
    attributes: Annotated[dict, Field(description='Data of the object.')]
    links: Annotated[Optional[dict], Field(default=None, description='Links.')]
    relationships: Annotated[Optional[dict], Field(default=None, description='Relationships.')]
