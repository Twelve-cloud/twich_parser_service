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
from domain.models import AggregateRoot, DomainModel


@dataclass(frozen=False)
class TwichGame(DomainModel, AggregateRoot[TwichGameDomainEvent]):
    """
    TwichGame: Class, representing twich game domain model. This class is an aggregate root.

    Bases:
        1) DomainModel: Base domain model. Every domain model should be inherited from this class.
        2) AggregateRoot[TwichGameDomainEvent]: Aggregate root.
           Every domain model that is aggregate root should be inhehited from this class.
    """

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
        """
        create: Classmethod that creates a twich game instance.
        It also produces event that twich game has been created.

        Args:
            id (int): ID of the twich game.
            name (str): Name of the twich game.
            igdb_id (str): ID of the twich game that is used by igdb.
            box_art_url (str): URL to the game's box art.
            parsed_at (datetime): Date and time when twich game has been parsed.

        Returns:
            TwichGame: Twich game instance.
        """

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
        """
        delete: Deletes a twich game instance.
        It also produces event that twich game has been deleted.
        """

        event: TwichGameDeleted = mapper.to(TwichGameDeleted).map(self)
        self.register_event(event)

        return
