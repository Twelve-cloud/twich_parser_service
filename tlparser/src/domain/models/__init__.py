"""
__init__.py: File, containing other model modules to simplify import.
"""


from domain.models.base import DomainModel
from domain.models.game import TwichGame
from domain.models.root import AggregateRoot
from domain.models.stream import TwichStream
from domain.models.user import TwichUser


__all__: list[str] = [
    'DomainModel',
    'TwichGame',
    'AggregateRoot',
    'TwichStream',
    'TwichUser',
]
