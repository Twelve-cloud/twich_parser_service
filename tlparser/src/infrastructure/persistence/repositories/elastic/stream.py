"""
stream.py: File, containing twich stream elastic repository implementation.
"""


from typing import Collection
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.models.elastic.stream import TwichStreamDAO


class TwichStreamElasticRepository(ITwichStreamRepository):
    """
    TwichStreamElasticRepository: Elastic implementation of ITwichStreamRepository.

    Args:
        ITwichStreamRepository: Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichStreamDAO.init()

    async def add_or_update(self, stream: TwichStream) -> None:
        """
        add_or_update: Add or update twich stream.

        Args:
            stream (TwichStream): Twich stream.
        """

        stream_persistence = mapper.to(TwichStreamDAO).map(stream)
        stream_persistence.meta.id = stream_persistence.id
        stream_persistence.save()

        return

    async def all(self) -> list[TwichStream]:
        """
        all: Return list of twich streams.

        Returns:
            list[TwichStream]: List of twich streams.
        """

        return [
            mapper.to(TwichStream).map(stream_persistence)
            for stream_persistence in TwichStreamDAO.search().query()
        ]

    async def delete(self, stream: TwichStream) -> None:
        """
        delete: Delete twich stream by user login.

        Args:
            stream (TwichStream): Twich stream.
        """

        TwichStreamDAO.search().query('match', user_login=stream.user_login).delete()

        return

    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        """
        get_stream_by_user_login: Return twich stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStream: Twich stream.
        """

        streams: Collection[TwichStreamDAO] = (
            TwichStreamDAO.search()
            .query(
                'match',
                user_login=user_login,
            )
            .execute()
        )

        if len(streams) == 0:
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(next(iter(streams)))
