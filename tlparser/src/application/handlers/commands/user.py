"""
user.py: File, containing command handler for a twich user.
"""


from application.commands import (
    DeleteTwichUserCommand,
    ParseTwichUserCommand,
)
from application.dto import FailureDTO, SuccessDTO
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichUserParser
from application.interfaces.publishers import ITwichUserPublisher
from application.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser


class ParseTwichUserCommandHandler(ICommandHandler[ParseTwichUserCommand]):
    def __init__(
        self,
        parser: ITwichUserParser,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        self.parser: ITwichUserParser = parser
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: ParseTwichUserCommand) -> SuccessDTO | FailureDTO:
        user: TwichUser = await self.parser.parse_user(command.login)
        await self.repository.add_or_update(user)
        await self.publisher.publish(user.pull_events())

        return SuccessDTO(status='Success')


class DeleteTwichUserCommandHandler(ICommandHandler[DeleteTwichUserCommand]):
    def __init__(
        self,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: DeleteTwichUserCommand) -> SuccessDTO | FailureDTO:
        user: TwichUser = await self.repository.get_user_by_login(command.login)
        user.delete()
        await self.repository.delete(user)
        await self.publisher.publish(user.pull_events())

        return SuccessDTO(status='Success')
