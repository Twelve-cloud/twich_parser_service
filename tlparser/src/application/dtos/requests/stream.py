"""
stream.py: File, containing twich stream requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class ParseTwichStreamRequest(BaseRequest):
    """
    ParseTwichStreamRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a stream.

    Args:
        BaseRequest: Base request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichStreamByUserLoginRequest(BaseRequest):
    """
    DeleteTwichStreamByUserLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a stream.

    Args:
        BaseRequest: Base request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichStreamByUserLoginRequest(BaseRequest):
    """
    GetTwichStreamByUserLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a stream.

    Args:
        BaseRequest: Base request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]
