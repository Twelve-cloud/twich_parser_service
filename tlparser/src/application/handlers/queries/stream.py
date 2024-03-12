"""
stream.py: File, containing twich stream query handlers.
"""


from automapper import mapper
from application import dto
from application.interfaces.handlers import IQueryHandler
from application.interfaces.repositories import ITwichStreamRepository
from application.queries import (
    GetAllTwichStreams,
    GetTwichStreamByUserLogin,
)
from domain.models import TwichStream


class GetTwichStreamByUserLoginHandler(IQueryHandler[GetTwichStreamByUserLogin, dto.TwichStream]):
    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetTwichStreamByUserLogin) -> dto.TwichStream:
        stream: TwichStream = await self.repository.get_stream_by_user_login(query.user_login)

        return mapper.to(dto.TwichStream).map(stream)


class GetAllTwichStreamsHandler(IQueryHandler[GetAllTwichStreams, dto.TwichStreams]):
    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetAllTwichStreams) -> dto.TwichStreams:
        streams: list[TwichStream] = await self.repository.all()

        return dto.TwichStreams(data=[mapper.to(dto.TwichStream).map(stream) for stream in streams])
