"""
user.py: File, containing twich user requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class ParseTwichUserRequest(BaseRequest):
    """
    ParseTwichUserRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a user.

    Args:
        BaseRequest: Base request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichUserByLoginRequest(BaseRequest):
    """
    DeleteTwichUserByLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a user.

    Args:
        BaseRequest: Base request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichUserByLoginRequest(BaseRequest):
    """
    GetTwichUserByLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a user.

    Args:
        BaseRequest: Base request class.
    """

    login: Annotated[str, Field(min_length=1, max_length=128)]
