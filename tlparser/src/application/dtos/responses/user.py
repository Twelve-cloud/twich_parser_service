"""
user.py: File, containing twich user responses.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.dtos.responses import BaseResponse


class ParseTwichUserResponse(BaseResponse):
    """
    ParseTwichUserResponse: Class, that represents DTO Response.
    This DTO Response represents user that has been parsed.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]
    login: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    display_name: Annotated[str, Field(min_length=0, max_length=128)]

    type: Annotated[str, Field()]
    broadcaster_type: Annotated[str, Field()]

    profile_image_url: Annotated[str, Field(min_length=0, max_length=256)]
    offline_image_url: Annotated[str, Field(min_length=0, max_length=256)]

    created_at: Annotated[datetime, Field()]
    parsed_at: Annotated[datetime, Field()]


class DeleteTwichUserByLoginResponse(BaseResponse):
    """
    DeleteTwichUserByLoginResponse: Class, that represents DTO Response.
    This DTO Response represents status when user has been deleted.

    Args:
        BaseResponse: Base response class.
    """

    status: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichUserByLoginResponse(BaseResponse):
    """
    GetTwichUserByLoginResponse: Class, that represents DTO Response.
    This DTO Response represents user that has been being getting.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]
    login: Annotated[str, Field(min_length=1, max_length=128)]
    description: Annotated[str, Field(min_length=0, max_length=4096)]
    display_name: Annotated[str, Field(min_length=0, max_length=128)]

    type: Annotated[str, Field()]
    broadcaster_type: Annotated[str, Field()]

    profile_image_url: Annotated[str, Field(min_length=0, max_length=256)]
    offline_image_url: Annotated[str, Field(min_length=0, max_length=256)]

    created_at: Annotated[datetime, Field()]
    parsed_at: Annotated[datetime, Field()]
