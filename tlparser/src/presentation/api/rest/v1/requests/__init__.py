"""
__init__.py: File, containing other request modules to simplify import.
"""


from presentation.api.rest.v1.requests.base import RequestSchema
from presentation.api.rest.v1.requests.post import JSONAPIPostSchema


__all__: list[str] = [
    'RequestSchema',
    'JSONAPIPostSchema',
]
