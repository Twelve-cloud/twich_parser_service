"""
user.py: File, containing twich user domain model.
"""


from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from automapper import mapper
from domain.events import (
    TwichUserCreated,
    TwichUserDeleted,
    TwichUserDomainEvent,
)
from domain.models.base import AggregateRoot, DomainModel


@dataclass(frozen=False)
class TwichUser(DomainModel, AggregateRoot[TwichUserDomainEvent]):
    """
    TwichUser: Class, representing twich user domain model. This class is an aggregate root.

    Bases:
        1) DomainModel: Base domain model. Every domain model should be inherited from this class.
        2) AggregateRoot[TwichUserDomainEvent]: Aggregate root.
           Every domain model that is aggregate root should be inhehited from this class.
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
        """
        create: Classmethod that creates a twich user instance.
        It also produces event that twich user has been created.

        Args:
            id (int): ID of the user.
            login (str): Login of the user.
            description (str): Description of the user profile.
            display_name (str): Display name of the user.
            type (str): Type of the user.
            broadcaster_type (str): Broadcaster type of the user.
            profile_image_url (str): URL to the user profile image.
            offline_image_url (str): URL to the user profile image when user is offline.
            created_at (datetime): Date and time when user has been created.
            parsed_at (datetime): Date and time when user has been parsed.

        Returns:
            TwichUser: Twich user instance.
        """

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

        event: TwichUserCreated = mapper.to(TwichUserCreated).map(user)
        user.register_event(event)

        return user

    def delete(self) -> None:
        """
        delete: Deletes a twich user instance.
        It also produces event that twich user has been deleted.
        """

        event: TwichUserDeleted = mapper.to(TwichUserDeleted).map(self)
        self.register_event(event)

        return
