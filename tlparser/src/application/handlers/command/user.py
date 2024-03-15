"""
user.py: File, containing command handler for a twich user.
"""


from application import dto
from application.commands import DeleteTwichUser, ParseTwichUser
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichUserParser
from application.interfaces.publishers import ITwichUserPublisher
from application.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser


class ParseTwichUserHandler(ICommandHandler[ParseTwichUser]):
    """
    ParseTwichUserHandler: Class, representing parse twich user command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[ParseTwichUser]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        parser: ITwichUserParser,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            parser (ITwichUserParser): Twich user parser.
            publisher (ITwichUserPublisher): Twich user publisher.
            repository (ITwichUserRepository): Twich user repository.
        """

        self.parser: ITwichUserParser = parser
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: ParseTwichUser) -> dto.Result:
        """
        handle: Handle parse twich user command.

        Args:
            command (ParseTwichUser): Command.

        Returns:
            dto.Result: Command handling result.
        """

        user: TwichUser = await self.parser.parse_user(command.login)
        await self.repository.add_or_update(user)
        await self.publisher.publish(user.pull_events())

        return dto.Result([{'id': user.id}, {'status': 'success'}])


class DeleteTwichUserHandler(ICommandHandler[DeleteTwichUser]):
    """
    DeleteTwichUserHandler: Class, representing delete twich user command handler.
    This class is interface implementation.

    Bases:
        1) ICommandHandler[DeleteTwichUser]: Command handler interface.
           Every command handler should implement this class.
    """

    def __init__(
        self,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            publisher (ITwichUserPublisher): Twich user publisher.
            repository (ITwichUserRepository): Twich user repository.
        """

        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: DeleteTwichUser) -> dto.Result:
        """
        handle: Handle delete twich user command.

        Args:
            command (DeleteTwichUser): Command.

        Returns:
            dto.Result: Command handling result.
        """

        user: TwichUser = await self.repository.get_user_by_login(command.login)
        user.delete()
        await self.repository.delete(user)
        await self.publisher.publish(user.pull_events())

        return dto.Result([{'status': 'success'}])
