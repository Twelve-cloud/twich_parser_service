"""
base.py: File, containing base response.
"""


from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    """
    BaseResponse: Class, that represents base response for all responses.
    It contains common settings for all responses.

    Args:
        BaseModel: Base class for base response class.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(strict=True, frozen=True, extra='forbid')
