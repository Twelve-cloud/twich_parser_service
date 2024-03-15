"""
stream.py: File, containing twich stream query handlers.
"""


from automapper import mapper
from application import dto
from application.interfaces.handlers import IQueryHandler
from application.interfaces.repositories import ITwichStreamRepository
from application.queries import GetAllTwichStreams, GetTwichStreamByUserLogin
from domain.models import TwichStream


class GetTwichStreamByUserLoginHandler(IQueryHandler[GetTwichStreamByUserLogin, dto.TwichStream]):
    """
    GetTwichStreamByUserLoginHandler: Class, representing get twich stream by ulogin query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetTwichStreamByUserLogin, dto.TwichStream]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetTwichStreamByUserLogin) -> dto.TwichStream:
        """
        handle: Should handle get twich stream by user login query.
        Must be overriden.

        Args:
            query (GetTwichStreamByUserLogin): Query.

        Returns:
            dto.TwichStream: Twich stream.
        """

        stream: TwichStream = await self.repository.get_stream_by_user_login(query.user_login)

        return mapper.to(dto.TwichStream).map(stream)


class GetAllTwichStreamsHandler(IQueryHandler[GetAllTwichStreams, dto.TwichStreams]):
    """
    GetAllTwichStreamsHandler: Class, representing get all twich streams query handler.
    This class is interface implementation.

    Bases:
        1) IQueryHandler[GetAllTwichStreams, dto.TwichStreams]: Query handler interface.
           Every query handler should implement this class.
    """

    def __init__(
        self,
        repository: ITwichStreamRepository,
    ) -> None:
        """
        __init__: Makes initialization.

        Args:
            repository (ITwichStreamRepository): Twich stream repository.
        """

        self.repository: ITwichStreamRepository = repository

    async def handle(self, query: GetAllTwichStreams) -> dto.TwichStreams:
        """
        handle: Should handle get all twich streams query.
        Must be overriden.

        Args:
            query (GetAllTwichStreams): Query.

        Returns:
            dto.TwichStreams: Twich streams.
        """

        streams: list[TwichStream] = await self.repository.all()

        return dto.TwichStreams(data=[mapper.to(dto.TwichStream).map(stream) for stream in streams])
