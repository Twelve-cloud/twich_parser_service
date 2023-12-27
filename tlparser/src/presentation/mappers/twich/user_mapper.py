"""
user_mapper.py: File, containing mapper for twich user.
"""


from domain.entities.twich.user_entity import TwichUserEntity
from presentation.schemas.twich.user_schema import TwichUserSchema


class TwichUserMapper:
    """
    TwichUserMapper: Class, that transform user schema to user domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichUserSchema) -> TwichUserEntity:
        """
        to_domain: Transform twich user read schema to twich user domain model.

        Args:
            schema (TwichUserSchema): Twich user read schema instance.

        Returns:
            TwichUserEntity: Twich domain model instance.
        """

        return TwichUserEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichUserEntity) -> TwichUserSchema:
        """
        to_schema: Transform twich user domain model to twich user read schema.

        Args:
            domain (TwichUserEntity): Twich user domain model instance.

        Returns:
            TwichUserSchema: Twich user read schema instance.
        """

        return TwichUserSchema.model_construct(
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
