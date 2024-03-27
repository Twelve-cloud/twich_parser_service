"""
stream.py: File, containing twich stream dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto.base import DTO


@dataclass(frozen=True)
class TwichStreamDTO(DTO):
    id: int
    user_id: int
    user_name: str
    user_login: str
    game_id: int
    game_name: str
    language: str
    title: str
    tags: list[str]
    started_at: datetime
    viewer_count: int
    type: str
    parsed_at: datetime
