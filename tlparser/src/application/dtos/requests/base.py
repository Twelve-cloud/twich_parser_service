"""
base.py: File, containing base request.
"""


from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class BaseRequest(BaseModel):
    """
    BaseRequest: Class, that represents base request for all requests.
    It contains common settings for all requests.

    Args:
        BaseModel: Base class for base request class.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(strict=True, frozen=True, extra='forbid')
