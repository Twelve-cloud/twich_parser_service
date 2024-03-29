"""
base.py: File, containing base schema.
"""


from typing import ClassVar
from pydantic import (
    BaseModel,
    ConfigDict,
)


class Schema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(strict=False, frozen=True, extra='ignore')
