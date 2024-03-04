"""
game.py: File, containing twich game requests.
"""


from typing import Annotated
from pydantic import Field
from application.dtos.requests import BaseRequest


class ParseTwichGameRequest(BaseRequest):
    """
    ParseTwichGameRequest: Class, that represents DTO Request.
    This DTO Request represents request to parse a game.

    Args:
        BaseRequest: Base request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]


class DeleteTwichGameByNameRequest(BaseRequest):
    """
    DeleteTwichGameByNameRequest: Class, that represents DTO Request.
    This DTO Request represents request to delete a game.

    Args:
        BaseRequest: Base request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]


class GetTwichGameByNameRequest(BaseRequest):
    """
    GetTwichGameByNameRequest: Class, that represents DTO Request.
    This DTO Request represents request to get a game.

    Args:
        BaseRequest: Base request class.
    """

    name: Annotated[str, Field(min_length=1, max_length=128)]
