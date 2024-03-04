"""
game.py: File, containing twich game responses.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.dtos.responses import BaseResponse


class ParseTwichGameResponse(BaseResponse):
    """
    ParseTwichGameResponse: Class, that represents DTO Response.
    This DTO Response represents game that has been parsed.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]
    parsed_at: Annotated[datetime, Field()]


class DeleteTwichGameByNameResponse(BaseResponse):
    """
    DeleteTwichGameByNameResponse: Class, that represents DTO Response.
    This DTO Response represents status when game has been deleted.

    Args:
        BaseResponse: Base response class.
    """

    status: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichGameByNameResponse(BaseResponse):
    """
    GetTwichGameByNameResponse: Class, that represents DTO Response.
    This DTO Response represents game that has been being getting.

    Args:
        BaseResponse: Base response class.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]
    parsed_at: Annotated[datetime, Field()]
