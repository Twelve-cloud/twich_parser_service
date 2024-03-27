"""
stream.py: File, containing twich stream query handlers.
"""


from automapper import mapper
from application.dto import TwichStreamDTO, TwichStreamsDTO
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

        return mapper.to(TwichStreamDTO).map(stream)


class GetAllTwichStreamsHandler(IQueryHandler[GetAllTwichStreams, TwichStreamsDTO]):
    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetAllTwichStreams) -> TwichStreamsDTO:
        streams: list[TwichStream] = await self.repository.all()

        return TwichStreamsDTO(data=[mapper.to(TwichStreamsDTO).map(stream) for stream in streams])
