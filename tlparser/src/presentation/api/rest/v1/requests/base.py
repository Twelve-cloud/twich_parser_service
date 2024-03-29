"""
base.py: File, containing base request schema.
"""


from typing import ClassVar
from pydantic import (
    BaseModel,
    ConfigDict,
)


class RequestSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(strict=False, frozen=True, extra='ignore')
