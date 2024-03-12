"""
__init__.py: File, containing other dto modules to simplify import.
"""


from application.dto.base import BaseDTO
from application.dto.game import (
    TwichGameDTO,
    TwichGamesDTO,
)
from application.dto.stream import (
    TwichStreamDTO,
    TwichStreamsDTO,
)
from application.dto.success import (
    SuccessDTO,
)
from application.dto.user import (
    TwichUserDTO,
    TwichUsersDTO,
)


__all__: list[str] = [
    'BaseDTO',
    'TwichGameDTO',
    'TwichGamesDTO',
    'TwichStreamDTO',
    'TwichStreamsDTO',
    'SuccessDTO',
    'TwichUserDTO',
    'TwichUsersDTO',
]
