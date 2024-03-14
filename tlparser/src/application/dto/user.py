"""
user.py: File, containing twich user dto.
"""


from dataclasses import dataclass
from datetime import datetime
from application.dto.base import DTO


@dataclass(frozen=True)
class TwichUser(DTO):
    """
    TwichUser: Class, representing twich user dto.

    Bases:
        1) DTO: Base DTO class. Every DTO should be inherited from this class.
    """

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
class TwichUsers(DTO):
    """
    TwichUsers: Class, representing twich users dto.

    Bases:
        1) DTO: Base DTO class. Every DTO should be inherited from this class.
    """

    data: list[TwichUser]
