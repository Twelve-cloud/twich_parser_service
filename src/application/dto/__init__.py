"""
__init__.py: File, containing other dto modules to simplify import.
"""


from typing import TypeVar

from application.dto.base import DTO
from application.dto.common import ResultDTO
from application.dto.game import (
    TwichGameDTO,
    TwichGamesDTO,
)
from application.dto.stream import (
    TwichStreamDTO,
    TwichStreamsDTO,
)
from application.dto.user import (
    TwichUserDTO,
    TwichUsersDTO,
)


RD = TypeVar('RD', bound=DTO)


__all__: list[str] = [
    'DTO',
    'ResultDTO',
    'TwichGameDTO',
    'TwichGamesDTO',
    'TwichStreamDTO',
    'TwichStreamsDTO',
    'TwichUserDTO',
    'TwichUsersDTO',
    'RD',
]
