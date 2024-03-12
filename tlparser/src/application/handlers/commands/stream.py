"""
stream.py: File, containing command handler for a twich stream.
"""


from application.commands import (
    DeleteTwichStreamCommand,
    ParseTwichStreamCommand,
)
from application.dto import FailureDTO, SuccessDTO
from application.interfaces.handlers import ICommandHandler
from application.interfaces.parsers import ITwichStreamParser
from application.interfaces.publishers import ITwichStreamPublisher
from application.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream


class ParseTwichStreamCommandHandler(ICommandHandler[ParseTwichStreamCommand]):
    def __init__(
        self,
        parser: ITwichStreamParser,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.parser: ITwichStreamParser = parser
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: ParseTwichStreamCommand) -> SuccessDTO | FailureDTO:
        stream: TwichStream = await self.parser.parse_stream(command.user_login)
        await self.repository.add_or_update(stream)
        await self.publisher.publish(stream.pull_events())

        return SuccessDTO(status='Success')


class DeleteTwichStreamCommandHandler(ICommandHandler[DeleteTwichStreamCommand]):
    def __init__(
        self,
        publisher: ITwichStreamPublisher,
        repository: ITwichStreamRepository,
    ) -> None:
        self.publisher: ITwichStreamPublisher = publisher
        self.repository: ITwichStreamRepository = repository

    async def handle(self, command: DeleteTwichStreamCommand) -> SuccessDTO | FailureDTO:
        stream: TwichStream = await self.repository.get_stream_by_user_login(command.user_login)
        stream.delete()
        await self.repository.delete(stream)
        await self.publisher.publish(stream.pull_events())

        return SuccessDTO(status='Success')
