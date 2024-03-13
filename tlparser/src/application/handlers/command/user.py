"""
user.py: File, containing command handler for a twich user.
"""


from application import dto
from application.commands import DeleteTwichUser, ParseTwichUser
from application.interfaces.handlers.command import ICommandHandler
from application.interfaces.parsers import ITwichUserParser
from application.interfaces.publishers import ITwichUserPublisher
from application.interfaces.repositories import ITwichUserRepository
from domain.models import TwichUser


class ParseTwichUserHandler(ICommandHandler[ParseTwichUser]):
    def __init__(
        self,
        parser: ITwichUserParser,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        self.parser: ITwichUserParser = parser
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: ParseTwichUser) -> dto.Result:
        user: TwichUser = await self.parser.parse_user(command.login)
        await self.repository.add_or_update(user)
        await self.publisher.publish(user.pull_events())

        return dto.Result([{'id': user.id}, {'status': 'success'}])


class DeleteTwichUserHandler(ICommandHandler[DeleteTwichUser]):
    def __init__(
        self,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: DeleteTwichUser) -> dto.Result:
        user: TwichUser = await self.repository.get_user_by_login(command.login)
        user.delete()
        await self.repository.delete(user)
        await self.publisher.publish(user.pull_events())

        return dto.Result([{'status': 'success'}])