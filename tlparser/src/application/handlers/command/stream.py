"""
stream.py: File, containing command handler for a twich stream.
"""


from application import dto
from application.commands import DeleteTwichStream, ParseTwichStream
from application.interfaces.handlers.command import ICommandHandler
from application.interfaces.parsers import ITwichStreamParser
from application.interfaces.publishers import ITwichStreamPublisher
from application.interfaces.repositories import ITwichStreamRepository
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

    async def handle(self, command: ParseTwichStream) -> dto.Result:
        stream: TwichStream = await self.parser.parse_stream(command.user_login)
        await self.repository.add_or_update(stream)
        await self.publisher.publish(stream.pull_events())

        return dto.Result([{'id': stream.id}, {'status': 'success'}])


class DeleteTwichStreamHandler(ICommandHandler[DeleteTwichStream]):
    def __init__(
        self,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: DeleteTwichStream) -> dto.Result:
        stream: TwichStream = await self.repository.get_stream_by_user_login(command.user_login)
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.pull_events())

        return dto.Result([{'status': 'success'}])
