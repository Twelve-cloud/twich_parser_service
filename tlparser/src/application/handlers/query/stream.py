"""
stream.py: File, containing twich stream query handlers.
"""


from dataclasses import asdict
from application.dto import TwichStreamDTO
from application.interfaces.handler import IQueryHandler
from application.interfaces.repository import ITwichStreamRepository
from application.queries import GetAllTwichStreams, GetTwichStreamByUserLogin
from domain.models import TwichStream


class GetTwichStreamByUserLoginHandler(IQueryHandler[GetTwichStreamByUserLogin, TwichStreamDTO]):
    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetTwichStreamByUserLogin) -> TwichStreamDTO:
        stream: TwichStream = await self.repository.get_stream_by_user_login(query.user_login)

        return TwichStreamDTO(**asdict(stream, dict_factory=TwichStream.as_dict))


class GetAllTwichStreamsHandler(IQueryHandler[GetAllTwichStreams, list[TwichStreamDTO]]):
    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetAllTwichStreams) -> list[TwichStreamDTO]:
        streams: list[TwichStream] = await self.repository.all()

        return [
            TwichStreamDTO(**asdict(stream, dict_factory=TwichStream.as_dict)) for stream in streams
        ]
