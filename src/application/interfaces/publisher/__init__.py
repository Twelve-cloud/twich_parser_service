"""
__init__.py: File, containing other publisher modules to simplify import.
"""


from application.interfaces.publisher.base import IPublisher
from application.interfaces.publisher.game import ITwichGamePublisher
from application.interfaces.publisher.stream import ITwichStreamPublisher
from application.interfaces.publisher.user import ITwichUserPublisher


__all__: list[str] = [
    'IPublisher',
    'ITwichGamePublisher',
    'ITwichStreamPublisher',
    'ITwichUserPublisher',
]
