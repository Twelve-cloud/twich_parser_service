"""
post.py: File, containing post request schema.
"""


from typing import Annotated
from pydantic import Field
from presentation.api.rest.v1.requests.base import RequestSchema


class JSONAPIPostRequestSchema(RequestSchema):
    type: Annotated[str, Field(description='Type of the object.')]
    attributes: Annotated[dict, Field(description='Data of the object.')]
