"""
stream.py: File, containing twich stream domain model.
"""


from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from automapper import mapper
from domain.events import (
    TwichStreamCreated,
    TwichStreamDeleted,
    TwichStreamDomainEvent,
)
from domain.models.base import AggregateRoot, DomainModel


@dataclass(frozen=False)
class TwichStream(DomainModel, AggregateRoot[TwichStreamDomainEvent]):
    """
    TwichStream: Class, representing twich stream domain model. This class is an aggregate root.

    Bases:
        1) DomainModel: Base domain model. Every domain model should be inherited from this class.
        2) AggregateRoot[TwichStreamDomainEvent]: Aggregate root.
           Every domain model that is aggregate root should be inhehited from this class.
    """

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
        create: Classmethod that creates a twich stream instance.
        It also produces event that twich stream has been created.

        Args:
            id (int): ID of the twich stream.
            user_id (int): ID of the user that is streaming.
            user_name (str): Name of the user that is streaming.
            user_login (str): Login of the user that is streaming.
            game_id (int): ID of the game that is being streamed.
            game_name (str): Name of the game that is being streamed.
            language (str): Language of the stream.
            title (str): Title of the stream.
            tags (list[str]): Tags of the stream.
            started_at (datetime): Date and time when stream has been started.
            viewer_count (int): Number of visitors.
            type (str): Type of the stream.
            parsed_at (datetime): Date and time when stream has been parsed.

        Returns:
            TwichStream: Twich stream instance.
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

        event: TwichStreamCreated = mapper.to(TwichStreamCreated).map(stream)
        stream.register_event(event)

        return stream

    def delete(self) -> None:
        """
        delete: Deletes a twich stream instance.
        It also produces event that twich stream has been deleted.
        """

        event: TwichStreamDeleted = mapper.to(TwichStreamDeleted).map(self)
        self.register_event(event)

        return
