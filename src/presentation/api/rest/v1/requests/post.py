"""
post.py: File, containing post request schema.
"""

from pydantic import Field

from presentation.api.rest.v1.requests.base import RequestSchema


class JSONAPIPostSchema(RequestSchema):
    type: str = Field(description='Type of the object.')
    attributes: dict = Field(description='Data of the object.')
