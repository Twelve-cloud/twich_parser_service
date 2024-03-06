"""
game.py: File, containing twich game elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.game import TwichGameDAO


class TwichGameElasticRepository(ITwichGameRepository):
    """
    TwichGameElasticRepository: Elastic implementation of ITwichGameRepository.

    Args:
        ITwichGameRepository: Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichGameDAO.init()

    async def add_or_update(self, game: TwichGame) -> None:
        """
        add_or_update: Add or update twich game.

        Args:
            game (TwichGame): Twich game.
        """

        game_persistence = mapper.to(TwichGameDAO).map(game)
        game_persistence.meta.id = game_persistence.id
        game_persistence.save()

        return

    async def all(self) -> list[TwichGame]:
        """
        all: Return list of twich games.

        Returns:
            list[TwichGame]: List of twich games.
        """

        return [
            mapper.to(TwichGame).map(game_persistence)
            for game_persistence in TwichGameDAO.search().query()
        ]

    async def delete(self, game: TwichGame) -> None:
        """
        delete: Delete twich game by name.

        Args:
            game (TwichGame): Twich game.
        """

        TwichGameDAO.search().query('match', name=game.name).delete()

        return

    async def get_game_by_name(self, name: str) -> TwichGame:
        """
        get_game_by_name: Return twich game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGame: Twich game.
        """

        games: Collection[TwichGameDAO] = TwichGameDAO.search().query('match', name=name).execute()

        if len(games) == 0:
            raise ObjectNotFoundException('Game is not found.')

        return mapper.to(TwichGame).map(next(iter(games)))
