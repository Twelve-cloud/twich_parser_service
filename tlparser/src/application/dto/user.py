"""
user.py: File, containing twich user dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto import DTO


@dataclass(frozen=True)
class TwichUserDTO(DTO):
    id: int
    login: str
    description: str
    display_name: str
    type: str
    broadcaster_type: str
    profile_image_url: str
    offline_image_url: str
    created_at: datetime
    parsed_at: datetime


@dataclass(frozen=True)
class TwichUsersDTO(DTO):
    users: list[TwichUserDTO]
