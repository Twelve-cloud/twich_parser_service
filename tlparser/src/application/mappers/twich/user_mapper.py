"""
user_mapper.py: File, containing mapper for twich user.
"""


from application.schemas.twich.user_schema import TwichUserCreateSchema, TwichUserReadSchema
from domain.entities.twich.user_entity import TwichUserEntity


class TwichUserCreateMapper:
    """
    TwichUserCreateMapper: Class, that transform user schema to user domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichUserCreateSchema) -> TwichUserEntity:
        """
        to_domain: Transform twich user create schema to twich user domain model.

        Args:
            schema (TwichUserCreateSchema): Twich user create schema instance.

        Returns:
            TwichUserEntity: Twich domain model instance.
        """

        return TwichUserEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichUserEntity) -> TwichUserCreateSchema:
        """
        to_schema: Transform twich user domain model to twich user create schema.

        Args:
            domain (TwichUserEntity): Twich user domain model instance.

        Returns:
            TwichUserCreateSchema: Twich user create schema instance.
        """

        return TwichUserCreateSchema.model_construct(
            id=domain.id,
            login=domain.login,
            description=domain.description,
            display_name=domain.display_name,
            type=domain.type,
            broadcaster_type=domain.broadcaster_type,
            profile_image_url=domain.profile_image_url,
            offline_image_url=domain.offline_image_url,
            created_at=domain.created_at,
        )


class TwichUserReadMapper:
    """
    TwichUserReadMapper: Class, that transform user schema to user domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichUserReadSchema) -> TwichUserEntity:
        """
        to_domain: Transform twich user read schema to twich user domain model.

        Args:
            schema (TwichUserReadSchema): Twich user read schema instance.

        Returns:
            TwichUserEntity: Twich domain model instance.
        """

        return TwichUserEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichUserEntity) -> TwichUserReadSchema:
        """
        to_schema: Transform twich user domain model to twich user read schema.

        Args:
            domain (TwichUserEntity): Twich user domain model instance.

        Returns:
            TwichUserReadSchema: Twich user read schema instance.
        """

        return TwichUserReadSchema.model_construct(
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
