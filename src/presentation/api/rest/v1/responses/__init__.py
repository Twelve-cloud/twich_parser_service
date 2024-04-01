"""
__init__.py: File, containing other response modules to simplify import.
"""


from presentation.api.rest.v1.responses.base import ResponseSchema
from presentation.api.rest.v1.responses.failure import JSONAPIFailureResponseSchema
from presentation.api.rest.v1.responses.success import JSONAPISuccessResponseSchema


__all__: list[str] = [
    'ResponseSchema',
    'JSONAPIFailureResponseSchema',
    'JSONAPISuccessResponseSchema',
]
