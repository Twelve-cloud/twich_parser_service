"""
stream.py: File, containing twich stream elastic repository implementation.
"""


from typing import Collection
from domain.exceptions.stream import StreamNotFoundException
from domain.exceptions.repositories.stream import ITwichStreamRepository
from domain.models.stream import TwichStream
from infrastructure.connections.elastic.database import ElasticSearchDatabase
from infrastructure.mappers.twich.elastic.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.elastic.stream_model import TwichStreamDAO


class TwichStreamElasticRepository(ITwichStreamRepository):
    """
    TwichStreamElasticRepository: Elastic implementation of ITwichStreamRepository.

    Args:
        ITwichStreamRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: ElasticSearchDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (ElasticSearchDatabase): ElasticDatabase instance, containing elastic connection.
        """

        self.db: ElasticSearchDatabase = db
        TwichStreamDAO.init()

    async def create_or_update(self, stream: TwichStream) -> None:
        """
        create_or_update: Create or update twich stream.

        Args:
            stream (TwichStream): Twich stream.
        """

        stream_persistence = TwichStreamMapper.to_persistence(stream)
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
            TwichStreamMapper.to_domain(stream_persistence)
            for stream_persistence in TwichStreamDAO.search().query()
        ]

    async def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream by user login.

        Args:
            user_login (str): Login of the user.
        """

        TwichStreamDAO.search().query('match', user_login=user_login).delete()

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
            raise StreamNotFoundException

        return TwichStreamMapper.to_domain(next(iter(streams)))
