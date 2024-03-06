"""
__init__.py: File, containing other request modules to simplify import.
"""


from application.dtos.requests.base import BaseRequest
from application.dtos.requests.game import (
    DeleteTwichGameByNameRequest,
    GetTwichGameByNameRequest,
    ParseTwichGameRequest,
    TwichGameRequest,
)
from application.dtos.requests.stream import (
    DeleteTwichStreamByUserLoginRequest,
    GetTwichStreamByUserLoginRequest,
    ParseTwichStreamRequest,
    TwichStreamRequest,
)
from application.dtos.requests.user import (
    DeleteTwichUserByLoginRequest,
    GetTwichUserByLoginRequest,
    ParseTwichUserRequest,
    TwichUserRequest,
)


__all__: list[str] = [
    'BaseRequest',
    'DeleteTwichGameByNameRequest',
    'GetTwichGameByNameRequest',
    'ParseTwichGameRequest',
    'TwichGameRequest',
    'DeleteTwichStreamByUserLoginRequest',
    'GetTwichStreamByUserLoginRequest',
    'ParseTwichStreamRequest',
    'TwichStreamRequest',
    'DeleteTwichUserByLoginRequest',
    'GetTwichUserByLoginRequest',
    'ParseTwichUserRequest',
    'TwichUserRequest',
]
