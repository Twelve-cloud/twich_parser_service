"""
user.py: File, containing twich user domain model.
"""


from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from domain.events import (
    TwichUserCreated,
    TwichUserDeleted,
    TwichUserDomainEvent,
)
from domain.models.agroot import AggregateRoot
from domain.models.base import DomainModel


@dataclass(frozen=False)
class TwichUser(DomainModel, AggregateRoot[TwichUserDomainEvent]):
    id: int
    login: str
    description: str
    display_name: str
    type: str
    broadcaster_type: str
    profile_image_url: str
    offline_image_url: str
    created_at: datetime

    @classmethod
    def create(
        cls,
        id: int,
        login: str,
        description: str,
        display_name: str,
        type: str,
        broadcaster_type: str,
        profile_image_url: str,
        offline_image_url: str,
        created_at: datetime,
        parsed_at: datetime,
        **kwargs: dict,
    ) -> TwichUser:
        user: TwichUser = cls(
            id=id,
            login=login,
            description=description,
            display_name=display_name,
            type=type,
            broadcaster_type=broadcaster_type,
            profile_image_url=profile_image_url,
            offline_image_url=offline_image_url,
            created_at=created_at,
            parsed_at=parsed_at,
        )

        event: TwichUserCreated = TwichUserCreated(
            id=id,
            login=login,
            description=description,
            display_name=display_name,
            type=type,
            broadcaster_type=broadcaster_type,
            profile_image_url=profile_image_url,
            offline_image_url=offline_image_url,
            created_at=created_at,
            parsed_at=parsed_at,
        )

        user.register_event(event)

        return user

    def delete(self) -> None:
        event: TwichUserDeleted = TwichUserDeleted(id=self.id)
        self.register_event(event)

        return
