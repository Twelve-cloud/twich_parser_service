"""
game.py: File, containing twich game domain model.
"""


from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from domain.events import (
    TwichGameCreated,
    TwichGameDeleted,
    TwichGameDomainEvent,
)
from domain.models.agroot import AggregateRoot
from domain.models.base import DomainModel


@dataclass(frozen=False)
class TwichGame(DomainModel, AggregateRoot[TwichGameDomainEvent]):
    id: int
    name: str
    igdb_id: str
    box_art_url: str

    @classmethod
    def create(
        cls,
        id: int,
        name: str,
        igdb_id: str,
        box_art_url: str,
        parsed_at: datetime,
        **kwargs: dict,
    ) -> TwichGame:
        game: TwichGame = cls(
            id=id,
            name=name,
            igdb_id=igdb_id,
            box_art_url=box_art_url,
            parsed_at=parsed_at,
        )

        event: TwichGameCreated = TwichGameCreated(
            id=game.id,
            name=game.name,
            igdb_id=game.igdb_id,
            box_art_url=game.box_art_url,
            parsed_at=game.parsed_at,
        )

        game.register_event(event)

        return game

    def delete(self) -> None:
        event: TwichGameDeleted = TwichGameDeleted(id=self.id)
        self.register_event(event)

        return
