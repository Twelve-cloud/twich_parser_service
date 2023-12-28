"""
game_service.py: File, containing service for a twich game.
"""


from application.mappers.twich.game_mapper import TwichGameMapper
from application.schemas.twich.game_schema import TwichGameSchema
from domain.entities.twich.game_entity import TwichGameEntity
from domain.events.twich.game_events import TwichGameCreatedOrUpdatedEvent
from domain.interfaces.publishers.twich.game_publisher import ITwichGamePublisher
from domain.interfaces.repositories.twich.game_repository import ITwichGameRepository
from domain.services.twich.game_service import TwichGameDomainService
from domain.types.types import ResultWithEvent


class TwichGameKafkaService:
    """
    TwichGameKafkaService: Class, that contains business logic for twich games.
    """

    def __init__(
        self,
        domain_service: TwichGameDomainService,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Do some initialization for TwichGameKafkaService class.

        Args:
            domain_service (TwichGameDomainService): Twich game domain service.
            publisher (ITwichGamePublisher): Twich game publisher.
            repository (ITwichGameRepository): Twich game repository.
        """

        self.domain_service: TwichGameDomainService = domain_service
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def parse_game(self, game_name: str) -> None:
        """
        parse_game: Called twich game publisher to publish event about parsing.

        Args:
            game_name (str): Name of the game.
        """

        await self.repository.parse_game(game_name)

        return

    async def private_parse_game(self, game_name: str) -> TwichGameSchema:
        """
        private_parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        game_entity: TwichGameEntity = await self.domain_service.parse_game(game_name)

        game_entity_with_event: ResultWithEvent[TwichGameEntity, TwichGameCreatedOrUpdatedEvent] = (
            await self.repository.create_or_update(game_entity)
        )

        return TwichGameMapper.to_schema(game_entity_with_event.result)

    async def create(self, schema: TwichGameSchema) -> None:
        """
        create: Create twich game.

        Args:
            schema (TwichGameSchema): Twich game schema.
        """

        await self.repository.create_or_update(TwichGameMapper.to_domain(schema))

    async def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delete twich game.

        Args:
            game_name (str): Name of the game.
        """

        await self.repository.delete_game_by_name(game_name)

        return

    async def get_all_games(self) -> list[TwichGameSchema]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[TwichGameSchema]: List of twich games.
        """

        return [
            TwichGameMapper.to_schema(game_entity) for game_entity in await self.repository.all()
        ]

    async def get_game_by_name(self, game_name: str) -> TwichGameSchema:
        """
        get_game_by_name: Return twich game by name.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameSchema: TwichGameSchema instance.
        """

        game_entity: TwichGameEntity = await self.repository.get_game_by_name(game_name)

        return TwichGameMapper.to_schema(game_entity)