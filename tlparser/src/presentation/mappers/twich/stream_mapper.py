"""
stream_mapper.py: File, containing mapper for twich stream.
"""


from domain.entities.twich.stream_entity import TwichStreamEntity
from presentation.schemas.twich.stream_schema import TwichStreamSchema


class TwichStreamMapper:
    """
    TwichStreamMapper: Class, that transform stream schema to stream domain model and vv.
    """

    @classmethod
    def to_domain(cls, schema: TwichStreamSchema) -> TwichStreamEntity:
        """
        to_domain: Transform twich stream read schema to twich stream domain model.

        Args:
            schema (TwichStreamSchema): Twich stream read schema instance.

        Returns:
            TwichStreamEntity: Twich domain model instance.
        """

        return TwichStreamEntity(**schema.model_dump())

    @classmethod
    def to_schema(cls, domain: TwichStreamEntity) -> TwichStreamSchema:
        """
        to_schema: Transform twich stream domain model to twich stream schema.

        Args:
            domain (TwichStreamEntity): Twich stream domain model instance.

        Returns:
            TwichStreamSchema: Twich stream read schema instance.
        """

        return TwichStreamSchema.model_construct(
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
