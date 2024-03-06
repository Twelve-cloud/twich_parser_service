"""
stream.py: File, containing twich stream mongo repository implementation.
"""


from typing import Optional
from automapper import mapper
from domain.exceptions import ObjectNotFoundException
from domain.interfaces.repositories import ITwichStreamRepository
from domain.models import TwichStream
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.models.mongo.stream import TwichStreamDAO


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

    async def add_or_update(self, stream: TwichStream) -> None:
        """
        add_or_update: Add or update twich stream.

        Args:
            stream (TwichStream): Twich stream.
        """

        stream_persistence = mapper.to(TwichStreamDAO).map(stream)
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
            for stream_persistence in TwichStreamDAO.objects
        ]

    async def delete(self, stream: TwichStream) -> None:
        """
        delete: Delete twich stream by user login.

        Args:
            stream (TwichStream): Twich stream.
        """

        for stream_persistence in TwichStreamDAO.objects(user_login=stream.user_login):
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
            raise ObjectNotFoundException('Stream is not found.')

        return mapper.to(TwichStream).map(stream_persistence)
