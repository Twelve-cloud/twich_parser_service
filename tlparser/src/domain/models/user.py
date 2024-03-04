"""
user.py: File, containing twich user domain model.
"""


from __future__ import annotations
from datetime import datetime
from automapper import mapper
from domain.events import (
    TwichUserCreatedEvent,
    TwichUserDeletedByLoginEvent,
    TwichUserDomainEvent,
)
from domain.models import BaseDomainModel


class TwichUser(BaseDomainModel[TwichUserDomainEvent]):
    """
    TwichUser: Class, that represents twich user domain model.

    Args:
        BaseDomainModel: Base domain model class.
    """

    def __init__(
        self,
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
    ) -> None:
        """
        __init__: Initialize twich user domain model instance.

        Args:
            id (int): Identifier of the user.
            login (str): Login of the user.
            description (str): Description of the user.
            display_name (str): Display name of the user.
            type (str): Type of the user.
            broadcaster_type (str): Broadcaster type of the user.
            profile_image_url (str): Profile image url of the user.
            offline_image_url (str): Offline image url of the user.
            created_at (datetime): Creation date of the user.
            parsed_at (datetime): Parsing date of the user.
        """

        super().__init__(parsed_at)

        self.id: int = id
        self.login: str = login
        self.description: str = description
        self.display_name: str = display_name
        self.type: str = type
        self.broadcaster_type: str = broadcaster_type
        self.profile_image_url: str = profile_image_url
        self.offline_image_url: str = offline_image_url
        self.created_at: datetime = created_at

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
        create: Create twich user domain model instance.
        Register domain event that represents that twich user has been created.

        Args:
            id (int): Identifier of the user.
            login (str): Login of the user.
            description (str): Description of the user.
            display_name (str): Display name of the user.
            type (str): Type of the user.
            broadcaster_type (str): Broadcaster type of the user.
            profile_image_url (str): Profile image url of the user.
            offline_image_url (str): Offline image url of the user.
            created_at (datetime): Creation date of the user.
            parsed_at (datetime): Parsing date of the user.

        Returns:
            TwichUser: Twich user domain model instance.
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

        event: TwichUserCreatedEvent = mapper.to(TwichUserCreatedEvent).map(user)
        user.register_event(event)

        return user

    def delete(self) -> None:
        """
        delete: Register domain event that represents that twich user has been deleted.
        """

        event: TwichUserDeletedByLoginEvent = mapper.to(TwichUserDeletedByLoginEvent).map(self)
        self.register_event(event)
