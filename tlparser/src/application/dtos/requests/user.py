"""
user.py: File, containing twich user requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class TwichUserRequest(BaseRequest):
    """
    TwichUserRequest: Class, that represents DTO Request.
    This DTO Request represents twich user request.

    Args:
        BaseRequest: Base request class.
    """

    pass


class ParseTwichUserRequest(TwichUserRequest):
    """
    ParseTwichUserRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a user.

    Args:
        TwichUserRequest: Twich user request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichUserByLoginRequest(TwichUserRequest):
    """
    DeleteTwichUserByLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a user.

    Args:
        TwichUserRequest: Twich user request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichUserByLoginRequest(TwichUserRequest):
    """
    GetTwichUserByLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a user.

    Args:
        TwichUserRequest: Twich user request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]
