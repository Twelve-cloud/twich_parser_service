"""
stream.py: File, containing twich stream domain model.
"""


from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from domain.events import (
    TwichStreamCreated,
    TwichStreamDeleted,
    TwichStreamDomainEvent,
)
from domain.models.agroot import AggregateRoot
from domain.models.base import DomainModel


@dataclass(frozen=False)
class TwichStream(DomainModel, AggregateRoot[TwichStreamDomainEvent]):
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

        event: TwichStreamCreated = TwichStreamCreated(
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

        stream.register_event(event)

        return stream

    def delete(self) -> None:
        event: TwichStreamDeleted = TwichStreamDeleted(id=self.id)
        self.register_event(event)

        return
