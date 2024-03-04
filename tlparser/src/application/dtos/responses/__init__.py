"""
__init__.py: File, containing other response modules to simplify import.
"""


from application.dtos.responses.base import BaseResponse
from application.dtos.responses.game import (
    DeleteTwichGameByNameResponse,
    GetTwichGameByNameResponse,
    ParseTwichGameResponse,
)
from application.dtos.responses.stream import (
    DeleteTwichStreamByUserLoginResponse,
    GetTwichStreamByUserLoginResponse,
    ParseTwichStreamResponse,
)
from application.dtos.responses.user import (
    DeleteTwichUserByLoginResponse,
    GetTwichUserByLoginResponse,
    ParseTwichUserResponse,
)


__all__: list[str] = [
    'BaseResponse',
    'DeleteTwichGameByNameResponse',
    'GetTwichGameByNameResponse',
    'ParseTwichGameResponse',
    'DeleteTwichStreamByUserLoginResponse',
    'GetTwichStreamByUserLoginResponse',
    'ParseTwichStreamResponse',
    'DeleteTwichUserByLoginResponse',
    'GetTwichUserByLoginResponse',
    'ParseTwichUserResponse',
]
