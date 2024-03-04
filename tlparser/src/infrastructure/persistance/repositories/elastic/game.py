"""
game.py: File, containing twich game elastic repository implementation.
"""


from typing import Collection
from domain.exceptions.game import GameNotFoundException
from domain.exceptions.repositories.game import ITwichGameRepository
from domain.models.game import TwichGame
from infrastructure.connections.elastic.database import ElasticSearchDatabase
from infrastructure.mappers.twich.elastic.game_mapper import TwichGameMapper
from infrastructure.models.twich.elastic.game_model import TwichGameDAO


class TwichGameElasticRepository(ITwichGameRepository):
    """
    TwichGameElasticRepository: Elastic implementation of ITwichGameRepository.

    Args:
        ITwichGameRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichGameDAO.init()

    async def create_or_update(self, game: TwichGame) -> None:
        """
        create_or_update: Create or update twich game.

        Args:
            game (TwichGame): Twich game.
        """

        game_persistence = TwichGameMapper.to_persistence(game)
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
            TwichGameMapper.to_domain(game_persistence)
            for game_persistence in TwichGameDAO.search().query()
        ]

    async def delete_game_by_name(self, name: str) -> None:
        """
        delete_game_by_name: Delete twich game by name.

        Args:
            name (str): Name of the game.

        Returns:
            TwichGameDeletedByNameEvent: Twich game deleted event.
        """

        TwichGameDAO.search().query('match', name=name).delete()

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
            raise GameNotFoundException

        return TwichGameMapper.to_domain(next(iter(games)))
