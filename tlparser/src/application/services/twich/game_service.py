"""
game_service.py: File, containing service for a twich game.
"""


from fastapi import status
from requests import Response, get
from application.dependencies.twich.token_dependency import TwichAPIToken
from common.config.twich.settings import settings
from domain.entities.twich.game_entity import TwichGameEntity
from domain.events.twich.game_events import (
    PublicParseGameCalledEvent,
    TwichGameCreatedOrUpdatedEvent,
    TwichGameDeletedByNameEvent,
)
from domain.exceptions.twich.game_exceptions import (
    GameNotFoundException,
    GetGameBadRequestException,
    GetGameUnauthorizedException,
)
from domain.publishers.twich.game_publisher import ITwichGamePublisher
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.twich.game_repository import ITwichGameRepository


class TwichGameService:
    """
    TwichGameService: Class, that contains business logic for twich games.
    """

    def __init__(
        self,
        repository: ITwichGameRepository,
        publisher: ITwichGamePublisher,
        token: TwichAPIToken,
    ) -> None:
        """
        __init__: Do some initialization for TwichGameService class.

        Args:
            repository (ITwichGameRepository): Twich game repository.
        """

        self.repository: ITwichGameRepository = repository
        self.publisher: ITwichGamePublisher = publisher
        self.access_token: str = token.access_token
        self.headers: dict[str, str] = token.headers

    async def parse_game(self, game_name: str) -> None:
        """
        parse_game: Called twich game publisher to publish event about parsing.

        Args:
            game_name (str): Name of the game.
        """

        event: PublicParseGameCalledEvent = self.repository.parse_game(game_name)

        self.publisher.publish_parse_game_called_event(event)

        return

    async def private_parse_game(self, game_name: str) -> TwichGameEntity:
        """
        private_parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Raises:
            GetGameBadRequestException: Raised when TwichAPI return 400 status code.
            GetGameUnauthorizedException: Raised when TwichAPI return 401 status code.
            GameNotFoundException: Raised when TwichAPI return no game.

        Returns:
            TwichGameEntity: TwichGameEntity instance.
        """

        response: Response = get(
            f'{settings.TWICH_GET_GAME_BASE_URL}?name={game_name}',
            headers=self.headers,
        )

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise GetGameBadRequestException

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise GetGameUnauthorizedException

        game_data: list = response.json().get('data')

        if not game_data:
            raise GameNotFoundException

        game_entity: TwichGameEntity = TwichGameEntity(**game_data[0])

        game: ResultWithEvent[TwichGameEntity, TwichGameCreatedOrUpdatedEvent] = (
            self.repository.create_or_update(game_entity)
        )

        game_event: TwichGameCreatedOrUpdatedEvent = game.event

        self.publisher.publish_created_or_updated_event(game_event)

        return game.result

    async def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delete twich game.

        Args:
            game_name (str): Name of the game.
        """

        event: TwichGameDeletedByNameEvent = self.repository.delete_game_by_name(game_name)

        self.publisher.publish_game_deleted_by_name_event(event)

        return

    async def get_all_games(self) -> list[TwichGameEntity]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[TwichGameEntity]: List of twich games.
        """

        return self.repository.all()

    async def get_game_by_name(self, game_name: str) -> TwichGameEntity:
        """
        get_game_by_name: Return twich game by name.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameEntity: TwichGameEntity instance.
        """

        game_entity: TwichGameEntity = self.repository.get_game_by_name(game_name)

        return game_entity
