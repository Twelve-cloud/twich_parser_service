"""
user_mapper.py: File, containig twich user mapper.
"""


from domain.entities.twich.user_entity import TwichUserEntity
from infrastructure.models.twich.mongo.user_model import TwichUser


class TwichUserMapper:
    """
    TwichUserMapper: Class, representing twich user mapper.
    """

    @classmethod
    def to_domain(self, persistence: TwichUser) -> TwichUserEntity:
        """
        to_domain: Transform persistence user model to domain user model.

        Args:
            persistence (TwichUser): Persistence user model.

        Returns:
            TwichUserEntity: Domain user model.
        """

        return TwichUserEntity(
            id=persistence.id,
            login=persistence.login,
            description=persistence.description,
            display_name=persistence.display_name,
            type=persistence.type,
            broadcaster_type=persistence.broadcaster_type,
            profile_image_url=persistence.profile_image_url,
            offline_image_url=persistence.offline_image_url,
            created_at=persistence.created_at,
            parsed_at=persistence.parsed_at,
        )

    @classmethod
    def to_persistence(self, domain: TwichUserEntity) -> TwichUser:
        """
        to_persistence: Transform domain user model to persistence user model.

        Args:
            domain (TwichUserEntity): Domain user model.

        Returns:
            TwichUser: Persistence user model.
        """

        return TwichUser(
            id=domain.id,
            login=domain.login,
            description=domain.description,
            display_name=domain.display_name,
            type=domain.type,
            broadcaster_type=domain.broadcaster_type,
            profile_image_url=domain.profile_image_url,
            offline_image_url=domain.offline_image_url,
            created_at=domain.created_at,
            parsed_at=domain.parsed_at,
        )
