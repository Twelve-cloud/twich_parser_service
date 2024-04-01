"""
__init__.py: File, containing other schema modules to simplify import.
"""


from presentation.api.rest.v1.schemas.base import Schema
from presentation.api.rest.v1.schemas.error import JSONAPIErrorSchema
from presentation.api.rest.v1.schemas.object import JSONAPIObjectSchema


__all__: list[str] = [
    'Schema',
    'JSONAPIErrorSchema',
    'JSONAPIObjectSchema',
]
