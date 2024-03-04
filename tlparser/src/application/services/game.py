"""
game.py: File, containing service implementation for a twich game.
"""


from automapper import mapper
from application.dtos.requests import (
    DeleteTwichGameByNameRequest,
    GetTwichGameByNameRequest,
    ParseTwichGameRequest,
)
from application.dtos.responses import (
    DeleteTwichGameByNameResponse,
    GetTwichGameByNameResponse,
    ParseTwichGameResponse,
)
from application.interfaces.services import ITwichGameService
from domain.interfaces.parsers import ITwichGameParser
from domain.interfaces.publishers import ITwichGamePublisher
from domain.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame


class TwichGameService(ITwichGameService):
    """
    TwichGameService: Class, that represents implementation of twich game service interface.
    That class unites presentation layer and infrastructure layer with domain layer.
    It calls repository, publisher and parser and return responses to controllers.
    """

    def __init__(
        self,
        parser: ITwichGameParser,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Initialize twich game service implementation class.

        Args:
            parser (ITwichGameParser): Twich game parser.
            publisher (ITwichGamePublisher): Twich game publisher.
            repository (ITwichGameRepository): Twich game repository.
        """

        self.parser: ITwichGameParser = parser
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def parse_game(
        self,
        request: ParseTwichGameRequest,
    ) -> ParseTwichGameResponse:
        """
        parse_game: Parse twich game and add it to repository.
        Also publish message about creating twich game.

        Args:
            request (ParseTwichGameRequest): Request about parsing twich game.

        Returns:
            ParseTwichGameResponse: Response about parsing twich game.
        """

        game: TwichGame = await self.parser.parse_game(**request.dict())
        await self.repository.add_or_update(game)
        await self.publisher.publish(game.events)

        return mapper.to(ParseTwichGameResponse).map(game)

    async def delete_game_by_name(
        self,
        request: DeleteTwichGameByNameRequest,
    ) -> DeleteTwichGameByNameResponse:
        """
        delete_game_by_name: Delete twich game and remove it from repository.
        Also publish message about deleting twich game.

        Args:
            request (DeleteTwichGameByNameRequest): Request about deleting twich game.

        Returns:
            DeleteTwichGameByNameResponse: Response about deleting twich game.
        """

        game: TwichGame = await self.repository.get_game_by_name(**request.dict())
        game.delete()
        await self.repository.delete(game)
        await self.publisher.publish(game.events)

        return DeleteTwichGameByNameResponse(status='OK')

    async def get_all_games(
        self,
    ) -> list[GetTwichGameByNameResponse]:
        """
        get_all_games: Return all twich games.

        Returns:
            list[GetTwichGameByNameResponse]: List of responses about getting twich game.
        """

        games: list[TwichGame] = await self.repository.all()

        return [mapper.to(GetTwichGameByNameResponse).map(game) for game in games]

    async def get_game_by_name(
        self,
        request: GetTwichGameByNameRequest,
    ) -> GetTwichGameByNameResponse:
        """
        get_game_by_name: Return twich game.

        Args:
            request (GetTwichGameByNameRequest): Request about getting twich game.

        Returns:
            GetTwichGameByNameResponse: Response about gettings twich game.
        """

        game: TwichGame = await self.repository.get_game_by_name(**request.dict())

        return mapper.to(GetTwichGameByNameResponse).map(game)
