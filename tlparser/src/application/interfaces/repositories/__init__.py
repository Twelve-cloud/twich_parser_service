"""
__init__.py: File, containing other repository interface modules to simplify import.
"""


from application.interfaces.repositories.base import IRepository
from application.interfaces.repositories.game import ITwichGameRepository
from application.interfaces.repositories.stream import ITwichStreamRepository
from application.interfaces.repositories.user import ITwichUserRepository


__all__: list[str] = [
    'IRepository',
    'ITwichGameRepository',
    'ITwichStreamRepository',
    'ITwichUserRepository',
]
