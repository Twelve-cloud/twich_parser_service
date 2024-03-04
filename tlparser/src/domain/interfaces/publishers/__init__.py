"""
__init__.py: File, containing other publisher modules to simplify import.
"""


from domain.interfaces.publishers.base import IBasePublisher
from domain.interfaces.publishers.game import ITwichGamePublisher
from domain.interfaces.publishers.stream import ITwichStreamPublisher
from domain.interfaces.publishers.user import ITwichUserPublisher


__all__: list[str] = [
    'IBasePublisher',
    'ITwichGamePublisher',
    'ITwichStreamPublisher',
    'ITwichUserPublisher',
]
