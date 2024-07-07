"""
__init__.py: File, containing other mongo models to simplify import.
"""


from infrastructure.persistence.models.mongo.base import BaseDAO
from infrastructure.persistence.models.mongo.game import TwichGameDAO
from infrastructure.persistence.models.mongo.stream import TwichStreamDAO
from infrastructure.persistence.models.mongo.user import TwichUserDAO


__all__: list[str] = [
    'BaseDAO',
    'TwichGameDAO',
    'TwichStreamDAO',
    'TwichUserDAO',
]
