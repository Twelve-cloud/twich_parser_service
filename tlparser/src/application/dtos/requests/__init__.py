"""
__init__.py: File, containing other request modules to simplify import.
"""


from application.dtos.requests.base import BaseRequest
from application.dtos.requests.game import (
    DeleteTwichGameByNameRequest,
    GetTwichGameByNameRequest,
    ParseTwichGameRequest,
)
from application.dtos.requests.stream import (
    DeleteTwichStreamByUserLoginRequest,
    GetTwichStreamByUserLoginRequest,
    ParseTwichStreamRequest,
)
from application.dtos.requests.user import (
    DeleteTwichUserByLoginRequest,
    GetTwichUserByLoginRequest,
    ParseTwichUserRequest,
)


__all__: list[str] = [
    'BaseRequest',
    'DeleteTwichGameByNameRequest',
    'GetTwichGameByNameRequest',
    'ParseTwichGameRequest',
    'DeleteTwichStreamByUserLoginRequest',
    'GetTwichStreamByUserLoginRequest',
    'ParseTwichStreamRequest',
    'DeleteTwichUserByLoginRequest',
    'GetTwichUserByLoginRequest',
    'ParseTwichUserRequest',
]
