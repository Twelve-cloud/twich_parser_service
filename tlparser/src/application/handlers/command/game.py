"""
game.py: File, containing command handler for a twich game.
"""


from application import dto
from application.commands import DeleteTwichGame, ParseTwichGame
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichGameParser
from application.interfaces.publishers import ITwichGamePublisher
from application.interfaces.repositories import ITwichGameRepository
from domain.models import TwichGame


class ParseTwichGameHandler(ICommandHandler[ParseTwichGame]):
    """
    ParseTwichGameHandler: Class, representing parse twich game command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[ParseTwichGame]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        parser: ITwichGameParser,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            parser (ITwichGameParser): Twich game parser.
            publisher (ITwichGamePublisher): Twich game publisher.
            repository (ITwichGameRepository): Twich game repository.
        """

        self.parser: ITwichGameParser = parser
        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: ParseTwichGame) -> dto.Result:
        """
        handle: Handle parse twich game command.

        Args:
            command (ParseTwichGame): Command.

        Returns:
            dto.Result: Command handling result.
        """

        game: TwichGame = await self.parser.parse_game(command.name)
        await self.repository.add_or_update(game)
        await self.publisher.publish(game.pull_events())

        return dto.Result([{'id': game.id}, {'status': 'success'}])


class DeleteTwichGameHandler(ICommandHandler[DeleteTwichGame]):
    """
    DeleteTwichGameHandler: Class, representing delete twich game command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[DeleteTwichGame]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        publisher: ITwichGamePublisher,
        repository: ITwichGameRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            publisher (ITwichGamePublisher): Twich game publisher.
            repository (ITwichGameRepository): Twich game repository.
        """

        self.publisher: ITwichGamePublisher = publisher
        self.repository: ITwichGameRepository = repository

    async def handle(self, command: DeleteTwichGame) -> dto.Result:
        """
        handle: Handle delete twich game command.

        Args:
            command (DeleteTwichGame): Command.

        Returns:
            dto.Result: Command handling result.
        """

        game: TwichGame = await self.repository.get_game_by_name(command.name)
        game.delete()
        await self.repository.delete(game)
        await self.publisher.publish(game.pull_events())

        return dto.Result([{'status': 'success'}])
