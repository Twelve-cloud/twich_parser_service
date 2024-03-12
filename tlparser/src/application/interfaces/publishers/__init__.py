"""
__init__.py: File, containing other publisher modules to simplify import.
"""


from application.interfaces.publishers.base import IPublisher
from application.interfaces.publishers.game import ITwichGamePublisher
from application.interfaces.publishers.stream import ITwichStreamPublisher
from application.interfaces.publishers.user import ITwichUserPublisher


__all__: list[str] = [
    'IPublisher',
    'ITwichGamePublisher',
    'ITwichStreamPublisher',
    'ITwichUserPublisher',
]
