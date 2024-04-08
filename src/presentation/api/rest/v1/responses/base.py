"""
base.py: File, containing base response schema.
"""


from typing import ClassVar

from pydantic import (
    BaseModel,
    ConfigDict,
)


class ResponseSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(strict=False, frozen=True, extra='ignore')
