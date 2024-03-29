"""
stream.py: File, containing command handler for a twich stream.
"""


from application.commands import (
    DeleteTwichStream,
    DeleteTwichStreamByUserLogin,
    ParseTwichStream,
)
from application.dto import ResultDTO
from application.interfaces.handler import ICommandHandler
from application.interfaces.parser import ITwichStreamParser
from application.interfaces.publisher import ITwichStreamPublisher
from application.interfaces.repository import ITwichStreamRepository
from domain.models import TwichStream


class ParseTwichStreamHandler(ICommandHandler[ParseTwichStream]):
    def __init__(
        self,
        parser: ITwichStreamParser,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.parser: ITwichStreamParser = parser
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: ParseTwichStream) -> ResultDTO:
        stream: TwichStream = await self.parser.parse_stream(command.user_login)
        await self.repository.add_or_update(stream)
        await self.publisher.publish(stream.pull_events())

        return ResultDTO(
            data={'id': stream.id},
            status='OK',
            description='Command has executed successfully.',
        )


class DeleteTwichStreamHandler(ICommandHandler[DeleteTwichStream]):
    def __init__(
        self,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: DeleteTwichStream) -> ResultDTO:
        stream: TwichStream = await self.repository.get_by_id(command.id)
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.pull_events())

        return ResultDTO(
            data={},
            status='OK',
            description='Command has executed successfully.',
        )


class DeleteTwichStreamByUserLoginHandler(ICommandHandler[DeleteTwichStreamByUserLogin]):
    def __init__(
        self,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: DeleteTwichStreamByUserLogin) -> ResultDTO:
        stream: TwichStream = await self.repository.get_stream_by_user_login(command.user_login)
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.pull_events())

        return ResultDTO(
            data={},
            status='OK',
            description='Command has executed successfully.',
        )
