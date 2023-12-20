"""
game_service.py: File, containing service for a twich game.
"""


from application.dependencies.twich.token_dependency import TwichAPIToken
from application.exceptions.twich.game_exceptions import (
    GameNotFoundException,
    GetGameBadRequestException,
    GetGameUnauthorizedException,
)
from application.mappers.twich.game_mapper import TwichGameCreateMapper, TwichGameReadMapper
from application.schemas.twich.game_schema import TwichGameCreateSchema, TwichGameReadSchema
from common.config.twich.settings import settings
from domain.entities.twich.game_entity import TwichGameEntity
from domain.repositories.twich.game_repository import TwichGameRepository
from fastapi import status
from requests import Response, get


class TwichGameService:
    """
    TwichGameService: Class, that contains business logic for twich games.
    """

    def __init__(self, repository: TwichGameRepository, token: TwichAPIToken) -> None:
        """
        __init__: Do some initialization for TwichGameService class.

        Args:
            repository (TwichGameRepository): Twich game repository.
        """

        self.repository = repository
        self.access_token = token.access_token
        self.headers = token.headers

    def parse_game(self, game_name: str) -> TwichGameReadSchema:
        """
        parse_game: Parse game data from the Twich.

        Args:
            game_name (str): Name of the game.

        Raises:
            GetGameBadRequestException: Raised when TwichAPI return 400 status code.
            GetGameUnauthorizedException: Raised when TwichAPI return 401 status code.
            GameNotFoundException: Raised when TwichAPI return no game.

        Returns:
            TwichGameReadSchema: TwichGameReadSchema instance.
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

        game_schema: TwichGameCreateSchema = TwichGameCreateSchema(**game_data[0])

        game_entity: TwichGameEntity = self.repository.create_or_update(
            TwichGameCreateMapper.to_domain(game_schema),
        )

        return TwichGameReadMapper.to_schema(game_entity)

    def delete_game_by_name(self, game_name: str) -> None:
        """
        delete_game_by_name: Delete twich game.

        Args:
            game_name (str): Name of the game.
        """

        self.repository.delete_game_by_name(game_name)

        return

    def get_all_games(self) -> list[TwichGameReadSchema]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[TwichGameReadSchema]: List of twich games.
        """

        return [TwichGameReadMapper.to_schema(game_entity) for game_entity in self.repository.all()]

    def get_game_by_name(self, game_name: str) -> TwichGameReadSchema:
        """
        get_game_by_name: Return twich game by name.

        Args:
            game_name (str): Name of the game.

        Returns:
            TwichGameReadSchema: TwichGameReadSchema instance.
        """

        game_entity: TwichGameEntity = self.repository.get_game_by_name(game_name)

        return TwichGameReadMapper.to_schema(game_entity)
