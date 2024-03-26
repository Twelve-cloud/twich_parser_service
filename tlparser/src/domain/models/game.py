"""
game.py: File, containing twich game domain model.
"""


from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from automapper import mapper
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

        event: TwichGameCreated = mapper.to(TwichGameCreated).map(game)
        game.register_event(event)

        return game

    def delete(self) -> None:
        event: TwichGameDeleted = mapper.to(TwichGameDeleted).map(self)
        self.register_event(event)

        return
