"""
game.py: File, containing twich game responses.
"""


from datetime import datetime
from typing import Annotated
from pydantic import Field
from application.dtos.responses import BaseResponse


class TwichGameResponse(BaseResponse):
    """
    TwichGameResponse: Class, that represents DTO Response.
    This DTO Response represents twich game response.

    Args:
        BaseResponse: Base response class.
    """

    pass


class ParseTwichGameResponse(TwichGameResponse):
    """
    ParseTwichGameResponse: Class, that represents DTO Response.
    This DTO Response represents game that has been parsed.

    Args:
        TwichGameResponse: Twich game response class.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]
    parsed_at: Annotated[datetime, Field()]


class DeleteTwichGameByNameResponse(TwichGameResponse):
    """
    DeleteTwichGameByNameResponse: Class, that represents DTO Response.
    This DTO Response represents status when game has been deleted.

    Args:
        TwichGameResponse: Twich game response class.
    """

    status: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichGameByNameResponse(TwichGameResponse):
    """
    GetTwichGameByNameResponse: Class, that represents DTO Response.
    This DTO Response represents game that has been being getting.

    Args:
        TwichGameResponse: Twich game response class.
    """

    id: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1, max_length=128)]
    igdb_id: Annotated[str, Field(min_length=0, max_length=128)]
    box_art_url: Annotated[str, Field(min_length=0, max_length=256)]
    parsed_at: Annotated[datetime, Field()]
