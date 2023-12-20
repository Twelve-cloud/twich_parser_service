"""
stream_repository.py: File, containing twich stream mongo repository implementation.
"""


from typing import Optional
from application.exceptions.twich.stream_exceptions import StreamNotFoundException
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.repositories.twich.stream_repository import TwichStreamRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.twich.mongo.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.mongo.stream_model import TwichStream


class TwichStreamMongoRepository(TwichStreamRepository):
    """
    TwichStreamMongoRepository: Mongo implementation of TwichStreamRepository.

    Args:
        TwichStreamRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db = db

    def create_or_update(self, stream_entity: TwichStreamEntity) -> TwichStreamEntity:
        """
        create_or_update: Create or update twich stream.

        Args:
            stream_entity (TwichStreamEntity): Twich stream entity.

        Returns:
            TwichStreamEntity: Created/Updated twich stream entity.
        """

        stream_persistence = TwichStreamMapper.to_persistence(stream_entity)
        stream_persistence.save()

        return TwichStreamMapper.to_domain(stream_persistence)

    def all(self) -> list[TwichStreamEntity]:
        """
        all: Return list of twich streams.

        Returns:
            list[TwichStreamEntity]: List of twich streams.
        """

        return [
            TwichStreamMapper.to_domain(stream_persistence)
            for stream_persistence in TwichStream.objects
        ]

    def delete_stream_by_user_login(self, user_login: str) -> None:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.
        """

        for stream_persistence in TwichStream.objects(user_login=user_login):
            stream_persistence.delete()

        return

    def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login: Return stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: Twich stream entity.
        """

        stream_persistence: Optional[TwichStream] = TwichStream.objects(
            user_login=user_login,
        ).first()

        if not stream_persistence:
            raise StreamNotFoundException

        return TwichStreamMapper.to_domain(stream_persistence)
