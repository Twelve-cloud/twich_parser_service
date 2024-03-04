"""
stream.py: File, containing twich stream domain model.
"""


from __future__ import annotations
from datetime import datetime
from automapper import mapper
from domain.events import (
    TwichStreamCreatedEvent,
    TwichStreamDeletedByUserLoginEvent,
    TwichStreamDomainEvent,
)
from domain.models import BaseDomainModel


class TwichStream(BaseDomainModel[TwichStreamDomainEvent]):
    """
    TwichStream: Class, that represents twich stream domain model.

    Args:
        BaseDomainModel: Base domain model class instantiated with twich stream domain event.
    """

    def __init__(
        self,
        id: int,
        user_id: int,
        user_name: str,
        user_login: str,
        game_id: int,
        game_name: str,
        language: str,
        title: str,
        tags: list[str],
        started_at: datetime,
        viewer_count: int,
        type: str,
        parsed_at: datetime,
    ) -> None:
        """
        __init__: Initialize twich stream domain model instance.

        Args:
            id (int): Identifier of the stream.
            user_id (int): Identifier of the user who has started the stream.
            user_name (str): Name of the user who has started the stream.
            user_login (str): Login of the user who has started the stream.
            game_id (int): Identifier of the game which has been streamed.
            game_name (str): Name of the game which has been streamed.
            language (str): Language of the stream.
            title (str): Title of the stream.
            tags (list[str]): Tags of the stream.
            started_at (datetime): Date when stream has been started.
            viewer_count (int): Number of viewers on the stream.
            type (str): Type of the stream.
            parsed_at (datetime): Parsing date of the stream.
        """

        super().__init__(parsed_at)

        self.id: int = id
        self.user_id: int = user_id
        self.user_name: str = user_name
        self.user_login: str = user_login
        self.game_id: int = game_id
        self.game_name: str = game_name
        self.language: str = language
        self.title: str = title
        self.tags: list[str] = tags
        self.started_at: datetime = started_at
        self.viewer_count: int = viewer_count
        self.type: str = type

    @classmethod
    def create(
        cls,
        id: int,
        user_id: int,
        user_name: str,
        user_login: str,
        game_id: int,
        game_name: str,
        language: str,
        title: str,
        tags: list[str],
        started_at: datetime,
        viewer_count: int,
        type: str,
        parsed_at: datetime,
        **kwargs: dict,
    ) -> TwichStream:
        """
        create: Create twich stream domain model instance.
        Register domain event that represents that twich stream has been created.

        Args:
            id (int): Identifier of the stream.
            user_id (int): Identifier of the user who has started the stream.
            user_name (str): Name of the user who has started the stream.
            user_login (str): Login of the user who has started the stream.
            game_id (int): Identifier of the game which has been streamed.
            game_name (str): Name of the game which has been streamed.
            language (str): Language of the stream.
            title (str): Title of the stream.
            tags (list[str]): Tags of the stream.
            started_at (datetime): Date when stream has been started.
            viewer_count (int): Number of viewers on the stream.
            type (str): Type of the stream.
            parsed_at (datetime): Parsing date of the stream.

        Returns:
            TwichStream: Twich stream domain model instance.
        """

        stream: TwichStream = cls(
            id=id,
            user_id=user_id,
            user_name=user_name,
            user_login=user_login,
            game_id=game_id,
            game_name=game_name,
            language=language,
            title=title,
            tags=tags,
            started_at=started_at,
            viewer_count=viewer_count,
            type=type,
            parsed_at=parsed_at,
        )

        event: TwichStreamCreatedEvent = mapper.to(TwichStreamCreatedEvent).map(stream)
        stream.register_event(event)

        return stream

    def delete(self) -> None:
        """
        delete: Register domain event that represents that twich stream has been deleted.
        """

        event: TwichStreamDeletedByUserLoginEvent = mapper.to(
            TwichStreamDeletedByUserLoginEvent
        ).map(self)
        self.register_event(event)
