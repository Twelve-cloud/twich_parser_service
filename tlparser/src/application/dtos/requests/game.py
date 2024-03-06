"""
game.py: File, containing twich game requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class TwichGameRequest(BaseRequest):
    """
    TwichGameRequest: Class, that represents DTO Request.
    This DTO Request represents twich game request.

    Args:
        BaseRequest: Base request class.
    """

    pass


class ParseTwichGameRequest(TwichGameRequest):
    """
    ParseTwichGameRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a game.

    Args:
        TwichGameRequest: Twich game request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichGameByNameRequest(TwichGameRequest):
    """
    DeleteTwichGameByNameRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a game.

    Args:
        TwichGameRequest: Twich game request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichGameByNameRequest(TwichGameRequest):
    """
    GetTwichGameByNameRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a game.

    Args:
        TwichGameRequest: Twich game request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]
