"""
game.py: File, containing command handler for a twich game.
"""


from application import dto
from application.commands import DeleteTwichGame, ParseTwichGame
from application.interfaces.handlers.command import ICommandHandler
from application.interfaces.parsers import ITwichGameParser
from application.interfaces.publishers import ITwichGamePublisher
from application.interfaces.repositories import ITwichGameRepository
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

    async def handle(self, command: ParseTwichGame) -> dto.Result:
        game: TwichGame = await self.parser.parse_game(command.name)
        await self.repository.add_or_update(game)
        await self.publisher.publish(game.pull_events())

        return dto.Result([{'id': game.id}, {'status': 'success'}])


class DeleteTwichGameHandler(ICommandHandler[DeleteTwichGame]):
    def __init__(
        self,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: DeleteTwichGame) -> dto.Result:
        game: TwichGame = await self.repository.get_game_by_name(command.name)
        game.delete()
        await self.repository.delete(game)
        await self.publisher.publish(game.pull_events())

        return dto.Result([{'status': 'success'}])
