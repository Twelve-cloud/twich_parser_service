"""
error.py: File, containing error schema.
"""


from typing import Optional

from pydantic import Field

from presentation.api.rest.v1.schemas.base import Schema


class JSONAPIErrorSchema(Schema):
    id: int = Field(description='ID of the error.')
    status: str = Field(description='Status of the error.')
    code: str = Field(description='Code of the error.')
    detail: str = Field(description='Detail of the error.')
    links: Optional[dict] = Field(default=None, description='Links.')
