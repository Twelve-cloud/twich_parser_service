"""
__init__.py: File, containing other repository modules to simplify import.
"""


from domain.interfaces.repositories.base import IRepository
from domain.interfaces.repositories.game import ITwichGameRepository
from domain.interfaces.repositories.stream import ITwichStreamRepository
from domain.interfaces.repositories.user import ITwichUserRepository


__all__: list[str] = [
    'IRepository',
    'ITwichGameRepository',
    'ITwichStreamRepository',
    'ITwichUserRepository',
]
