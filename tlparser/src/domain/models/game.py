"""
game.py: File, containing twich game domain model.
"""


from __future__ import annotations
from datetime import datetime
from automapper import mapper
from domain.events import (
    TwichGameCreatedEvent,
    TwichGameDeletedEvent,
    TwichGameDomainEvent,
)
from domain.models import BaseDomainModel


class TwichGame(BaseDomainModel[TwichGameDomainEvent]):
    """
    TwichGame: Class, that reprensents twich game domain model.

    Args:
        BaseDomainModel: Base domain model class instantiated with twich game domain event.
    """

    def __init__(
        self,
        id: int,
        name: str,
        igdb_id: str,
        box_art_url: str,
        parsed_at: datetime,
    ) -> None:
        """
        __init__: Initialize twich game domain model instance.

        Args:
            id (int): Identifier of the game.
            name (str): Name of the game.
            igdb_id (str): Igdb identifier of the game.
            box_art_url (str): Url to game image.
            parsed_at (datetime): Parsing date of the game.
        """

        super().__init__(parsed_at)

        self.id: int = id
        self.name: str = name
        self.igdb_id: str = igdb_id
        self.box_art_url: str = box_art_url

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
        create: Create twich game domain model instance.
        Register domain event that represents that twich game has been created.

        Args:
            id (int): Identifier of the game.
            name (str): Name of the game.
            igdb_id (str): Igdb identifier of the game.
            box_art_url (str): Url to game image.
            parsed_at (datetime): Parsing date of the game.

        Returns:
            TwichGame: Twich game domain model instance.
        """

        game: TwichGame = cls(
            id=id,
            name=name,
            igdb_id=igdb_id,
            box_art_url=box_art_url,
            parsed_at=parsed_at,
        )

        event: TwichGameCreatedEvent = mapper.to(TwichGameCreatedEvent).map(game)
        game.register_event(event)

        return game

    def delete(self) -> None:
        """
        delete: Register domain event that represents that twich game has been deleted.
        """

        event: TwichGameDeletedEvent = mapper.to(TwichGameDeletedEvent).map(self)
        self.register_event(event)
