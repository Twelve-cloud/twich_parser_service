"""
stream_mapper.py: File, containig twich stream mapper.
"""


from domain.entities.twich.stream_entity import TwichStreamEntity
from infrastructure.models.twich.mongo.stream_model import TwichStream


class TwichStreamMapper:
    """
    TwichStreamMapper: Class, representing twich stream mapper.
    """

    @classmethod
    def to_domain(self, persistence: TwichStream) -> TwichStreamEntity:
        """
        to_domain: Transform persistence stream model to domain stream model.

        Args:
            persistence (TwichStream): Persistence stream model.

        Returns:
            TwichStreamEntity: Domain stream model.
        """

        return TwichStreamEntity(
            id=persistence.id,
            user_id=persistence.user_id,
            user_name=persistence.user_name,
            user_login=persistence.user_login,
            game_id=persistence.game_id,
            game_name=persistence.game_name,
            language=persistence.language,
            title=persistence.title,
            tags=persistence.tags,
            started_at=persistence.started_at,
            viewer_count=persistence.viewer_count,
            type=persistence.type,
            parsed_at=persistence.parsed_at,
        )

    @classmethod
    def to_persistence(self, domain: TwichStreamEntity) -> TwichStream:
        """
        to_persistence: Transform domain stream model to persistence stream model.

        Args:
            domain (TwichStreamEntity): Domain stream model.

        Returns:
            TwichStream: Persistence stream model.
        """

        return TwichStream(
            id=domain.id,
            user_id=domain.user_id,
            user_name=domain.user_name,
            user_login=domain.user_login,
            game_id=domain.game_id,
            game_name=domain.game_name,
            language=domain.language,
            title=domain.title,
            tags=domain.tags,
            started_at=domain.started_at,
            viewer_count=domain.viewer_count,
            type=domain.type,
            parsed_at=domain.parsed_at,
        )
