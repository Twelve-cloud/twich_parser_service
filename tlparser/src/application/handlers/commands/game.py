"""
game.py: File, containing command handler for a twich game.
"""


from application.commands import (
    DeleteTwichGameCommand,
    ParseTwichGameCommand,
)
from application.dto import FailureDTO, SuccessDTO
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichGameParser
from application.interfaces.publishers import ITwichGamePublisher
from application.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame


class ParseTwichGameCommandHandler(ICommandHandler[ParseTwichGameCommand]):
    def __init__(
        self,
        parser: ITwichGameParser,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        self.parser: ITwichGameParser = parser
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: ParseTwichGameCommand) -> SuccessDTO | FailureDTO:
        game: TwichGame = await self.parser.parse_game(command.name)
        await self.repository.add_or_update(game)
        await self.publisher.publish(game.pull_events())

        return SuccessDTO(status='Success')


class DeleteTwichGameCommandHandler(ICommandHandler[DeleteTwichGameCommand]):
    def __init__(
        self,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: DeleteTwichGameCommand) -> SuccessDTO | FailureDTO:
        game: TwichGame = await self.repository.get_game_by_name(command.name)
        game.delete()
        await self.repository.delete(game)
        await self.publisher.publish(game.pull_events())

        return SuccessDTO(status='Success')
