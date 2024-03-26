"""
__init__.py: File, containing other repository interface modules to simplify import.
"""


from application.interfaces.repository.base import IRepository
from application.interfaces.repository.game import ITwichGameRepository
from application.interfaces.repository.stream import ITwichStreamRepository
from application.interfaces.repository.user import ITwichUserRepository


__all__: list[str] = [
    'IRepository',
    'ITwichGameRepository',
    'ITwichStreamRepository',
    'ITwichUserRepository',
]
