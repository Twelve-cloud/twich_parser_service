"""
__init__.py: File, containing other postgres models to simplify import.
"""


from infrastructure.persistence.models.postgres.base import BaseDAO
from infrastructure.persistence.models.postgres.game import TwichGameDAO
from infrastructure.persistence.models.postgres.stream import TwichStreamDAO
from infrastructure.persistence.models.postgres.user import TwichUserDAO


__all__: list[str] = [
    'BaseDAO',
    'TwichGameDAO',
    'TwichStreamDAO',
    'TwichUserDAO',
]
