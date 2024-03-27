"""
user.py: File, containing command handler for a twich user.
"""


from application.dto import ResultDTO
from application.commands import DeleteTwichUser, ParseTwichUser
from application.interfaces.handler import ICommandHandler
from application.interfaces.parser import ITwichUserParser
from application.interfaces.publisher import ITwichUserPublisher
from application.interfaces.repository import ITwichUserRepository
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

    async def handle(self, command: ParseTwichUser) -> ResultDTO:
        user: TwichUser = await self.parser.parse_user(command.login)
        await self.repository.add_or_update(user)
        await self.publisher.publish(user.pull_events())

        return ResultDTO([{'id': user.id}, {'status': 'success'}])


class DeleteTwichUserHandler(ICommandHandler[DeleteTwichUser]):
    def __init__(
        self,
        publisher: ITwichUserPublisher,
        repository: ITwichUserRepository,
    ) -> None:
        self.publisher: ITwichUserPublisher = publisher
        self.repository: ITwichUserRepository = repository

    async def handle(self, command: DeleteTwichUser) -> ResultDTO:
        user: TwichUser = await self.repository.get_user_by_login(command.login)
        user.delete()
        await self.repository.delete(user)
        await self.publisher.publish(user.pull_events())

        return ResultDTO([{'status': 'success'}])
