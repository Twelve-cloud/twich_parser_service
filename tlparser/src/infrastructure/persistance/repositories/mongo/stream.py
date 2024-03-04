"""
stream.py: File, containing twich stream mongo repository implementation.
"""


from typing import Optional
from domain.exceptions.stream import StreamNotFoundException
from domain.exceptions.repositories.stream import ITwichStreamRepository
from domain.models.stream import TwichStream
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.mongo.stream_model import TwichStreamDAO


class TwichStreamMongoRepository(ITwichStreamRepository):
    """
    TwichStreamMongoRepository: Mongo implementation of ITwichStreamRepository.

    Args:
        ITwichStreamRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db: MongoDatabase = db

    async def create_or_update(self, stream: TwichStream) -> None:
        """
        create_or_update: Create or update twich stream.

        Args:
            stream (TwichStream): Twich stream.
        """

        stream_persistence = TwichStreamMapper.to_persistence(stream)
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
            for stream_persistence in TwichStreamDAO.objects
        ]

    async def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete twich stream by user login.

        Args:
            user_login (str): Login of the user.
        """

        for stream_persistence in TwichStreamDAO.objects(user_login=user_login):
            stream_persistence.delete()

        return

    async def get_stream_by_user_login(self, user_login: str) -> TwichStream:
        """
        get_stream_by_user_login: Return twich stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStream: Twich stream.
        """

        stream_persistence: Optional[TwichStreamDAO] = TwichStreamDAO.objects(
            user_login=user_login,
        ).first()

        if not stream_persistence:
            raise StreamNotFoundException

        return TwichStreamMapper.to_domain(stream_persistence)
