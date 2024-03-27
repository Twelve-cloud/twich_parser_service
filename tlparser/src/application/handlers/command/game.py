"""
game.py: File, containing command handler for a twich game.
"""


from application.commands import DeleteTwichGame, ParseTwichGame
from application.dto import ResultDTO
from application.interfaces.handler import ICommandHandler
from application.interfaces.parser import ITwichGameParser
from application.interfaces.publisher import ITwichGamePublisher
from application.interfaces.repository import ITwichGameRepository
from domain.models import TwichGame


class ParseTwichGameHandler(ICommandHandler[ParseTwichGame]):
    def __init__(
        self,
        parser: ITwichGameParser,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        self.parser: ITwichGameParser = parser
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: ParseTwichGame) -> ResultDTO:
        game: TwichGame = await self.parser.parse_game(command.name)
        await self.repository.add_or_update(game)
        await self.publisher.publish(game.pull_events())

        return ResultDTO([{'id': game.id}, {'status': 'success'}])


class DeleteTwichGameHandler(ICommandHandler[DeleteTwichGame]):
    def __init__(
        self,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: DeleteTwichGame) -> ResultDTO:
        game: TwichGame = await self.repository.get_game_by_name(command.name)
        game.delete()
        await self.repository.delete(game)
        await self.publisher.publish(game.pull_events())

        return ResultDTO([{'status': 'success'}])
