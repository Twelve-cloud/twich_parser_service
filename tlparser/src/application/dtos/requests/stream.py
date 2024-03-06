"""
stream.py: File, containing twich stream requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class TwichStreamRequest(BaseRequest):
    """
    TwichStreamRequest: Class, that represents DTO Request.
    This DTO Request represents twich stream request.

    Args:
        BaseRequest: Base request class.
    """

    pass


class ParseTwichStreamRequest(TwichStreamRequest):
    """
    ParseTwichStreamRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a stream.

    Args:
        TwichStreamRequest: Twich stream request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichStreamByUserLoginRequest(TwichStreamRequest):
    """
    DeleteTwichStreamByUserLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a stream.

    Args:
        TwichStreamRequest: Twich stream request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichStreamByUserLoginRequest(TwichStreamRequest):
    """
    GetTwichStreamByUserLoginRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a stream.

    Args:
        TwichStreamRequest: Twich stream request class.
    """

    user_login: Annotated[str, Field(min_length=1, max_length=128)]
