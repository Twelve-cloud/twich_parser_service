"""
object.py: File, containing object schema.
"""


from typing import Optional
from pydantic import Field
from presentation.api.rest.v1.schemas.base import Schema


class JSONAPIObjectSchema(Schema):
    id: int = Field(description='ID of the object.')
    type: str = Field(description='Type of the object.')
    attributes: dict = Field(description='Data of the object.')
    links: Optional[dict] = Field(default=None, description='Links.')
    relationships: Optional[dict] = Field(default=None, description='Relationships.')
