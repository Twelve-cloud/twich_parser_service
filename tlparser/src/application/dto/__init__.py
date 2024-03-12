"""
__init__.py: File, containing other dto modules to simplify import.
"""


from application.dto.base import DTO
from application.dto.game import (
    TwichGame,
    TwichGames,
)
from application.dto.stream import (
    TwichStream,
    TwichStreams,
)
from application.dto.success import (
    Failure,
    Success,
)
from application.dto.user import (
    TwichUser,
    TwichUsers,
)


__all__: list[str] = [
    'DTO',
    'TwichGame',
    'TwichGames',
    'TwichStream',
    'TwichStreams',
    'Failure',
    'Success',
    'TwichUser',
    'TwichUsers',
]
