"""
__init__.py: File, containing other response modules to simplify import.
"""


from application.dtos.responses.base import BaseResponse
from application.dtos.responses.game import (
    DeleteTwichGameByNameResponse,
    GetTwichGameByNameResponse,
    ParseTwichGameResponse,
    TwichGameResponse,
)
from application.dtos.responses.stream import (
    DeleteTwichStreamByUserLoginResponse,
    GetTwichStreamByUserLoginResponse,
    ParseTwichStreamResponse,
    TwichStreamResponse,
)
from application.dtos.responses.user import (
    DeleteTwichUserByLoginResponse,
    GetTwichUserByLoginResponse,
    ParseTwichUserResponse,
    TwichUserResponse,
)


__all__: list[str] = [
    'BaseResponse',
    'DeleteTwichGameByNameResponse',
    'GetTwichGameByNameResponse',
    'ParseTwichGameResponse',
    'TwichGameResponse',
    'DeleteTwichStreamByUserLoginResponse',
    'GetTwichStreamByUserLoginResponse',
    'ParseTwichStreamResponse',
    'TwichStreamResponse',
    'DeleteTwichUserByLoginResponse',
    'GetTwichUserByLoginResponse',
    'ParseTwichUserResponse',
    'TwichUserResponse',
]
