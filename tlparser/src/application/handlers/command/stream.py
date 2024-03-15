"""
stream.py: File, containing command handler for a twich stream.
"""


from application import dto
from application.commands import DeleteTwichStream, ParseTwichStream
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichStreamParser
from application.interfaces.publishers import ITwichStreamPublisher
from application.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream


class ParseTwichStreamHandler(ICommandHandler[ParseTwichStream]):
    """
    ParseTwichStreamHandler: Class, representing parse twich stream command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[ParseTwichStream]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        parser: ITwichStreamParser,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            parser (ITwichStreamParser): Twich stream parser.
            publisher (ITwichStreamPublisher): Twich stream publisher.
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.parser: ITwichStreamParser = parser
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: ParseTwichStream) -> dto.Result:
        """
        handle: Handle parse twich stream command.

        Args:
            command (ParseTwichStream): Command.

        Returns:
            dto.Result: Command handling result.
        """

        stream: TwichStream = await self.parser.parse_stream(command.user_login)
        await self.repository.add_or_update(stream)
        await self.publisher.publish(stream.pull_events())

        return dto.Result([{'id': stream.id}, {'status': 'success'}])


class DeleteTwichStreamHandler(ICommandHandler[DeleteTwichStream]):
    """
    DeleteTwichStreamHandler: Class, representing delete twich stream command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[DeleteTwichStream]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            publisher (ITwichStreamPublisher): Twich stream publisher.
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: DeleteTwichStream) -> dto.Result:
        """
        handle: Handle delete twich stream command.

        Args:
            command (DeleteTwichStream): Command.

        Returns:
            dto.Result: Command handling result.
        """

        stream: TwichStream = await self.repository.get_stream_by_user_login(command.user_login)
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.pull_events())

        return dto.Result([{'status': 'success'}])
