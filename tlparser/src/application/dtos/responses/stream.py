"""
stream.py: File, containing twich stream responses.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.dtos.responses import BaseResponse


class ParseTwichStreamResponse(BaseResponse):
    """
    ParseTwichStreamResponse: Class, that represents DTO Response.
    This DTO Response represents stream that has been parsed.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]

    user_id: Annotated[int, Field(ge=0)]
    user_name: Annotated[str, Field(min_length=1, max_length=128)]
    user_login: Annotated[str, Field(min_length=1, max_length=128)]

    game_id: Annotated[int, Field(ge=0)]
    game_name: Annotated[str, Field(min_length=1, max_length=128)]

    language: Annotated[str, Field(min_length=0, max_length=128)]
    title: Annotated[str, Field(min_length=0, max_length=128)]

    tags: Annotated[list[str], Field()]
    started_at: Annotated[datetime, Field()]
    viewer_count: Annotated[int, Field(ge=0)]
    type: Annotated[str, Field()]
    parsed_at: Annotated[datetime, Field()]


class DeleteTwichStreamByUserLoginResponse(BaseResponse):
    """
    DeleteTwichStreamByUserLoginResponse: Class, that represents DTO Response.
    This DTO Response represents status when stream has been deleted.

    Args:
        BaseResponse: Base response class.
    """

    status: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichStreamByUserLoginResponse(BaseResponse):
    """
    GetTwichStreamByUserLoginResponse: Class, that represents DTO Response.
    This DTO Response represents stream that has been being getting.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]

    user_id: Annotated[int, Field(ge=0)]
    user_name: Annotated[str, Field(min_length=1, max_length=128)]
    user_login: Annotated[str, Field(min_length=1, max_length=128)]

    game_id: Annotated[int, Field(ge=0)]
    game_name: Annotated[str, Field(min_length=1, max_length=128)]

    language: Annotated[str, Field(min_length=0, max_length=128)]
    title: Annotated[str, Field(min_length=0, max_length=128)]

    tags: Annotated[list[str], Field()]
    started_at: Annotated[datetime, Field()]
    viewer_count: Annotated[int, Field(ge=0)]
    type: Annotated[str, Field()]
    parsed_at: Annotated[datetime, Field()]
