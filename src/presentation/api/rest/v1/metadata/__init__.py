"""
__init__.py: File, containing other metadata modules to simplify import.
"""


from presentation.api.rest.v1.metadata.game import TwichGameMetadata
from presentation.api.rest.v1.metadata.stream import TwichStreamMetadata
from presentation.api.rest.v1.metadata.user import TwichUserMetadata


__all__: list[str] = [
    'TwichGameMetadata',
    'TwichStreamMetadata',
    'TwichUserMetadata',
]
