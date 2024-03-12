"""
__init__.py: File, containing other dto modules to simplify import.
"""


from application.dto.base import DTO
from application.dto.common import Result
from application.dto.game import (
    TwichGame,
    TwichGames,
)
from application.dto.stream import (
    TwichStream,
    TwichStreams,
)
from application.dto.user import (
    TwichUser,
    TwichUsers,
)


__all__: list[str] = [
    'DTO',
    'Result',
    'TwichGame',
    'TwichGames',
    'TwichStream',
    'TwichStreams',
    'TwichUser',
    'TwichUsers',
]
