"""
test_user_mapper.py: File, containing tests for user mapper.
"""


from datetime import datetime
from application.mappers.twich.user_mapper import TwichUserMapper
from application.schemas.twich.user_schema import TwichUserSchema
from domain.entities.twich.user_entity import TwichUserEntity


class TestLamodaProductMapper:
    def test_to_domain(self):
        schema = TwichUserSchema(
            id=1,
            login='login',
            description='description',
            display_name='display_name',
            type='admin',
            broadcaster_type='affiliate',
            profile_image_url='profile_image_url',
            offline_image_url='offline_image_url',
            created_at=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        entity = TwichUserMapper.to_domain(schema)

        assert entity.id == schema.id
        assert entity.parsed_at == schema.parsed_at

    def test_to_schema(self):
        entity = TwichUserEntity(
            id=1,
            login='login',
            description='description',
            display_name='display_name',
            type='admin',
            broadcaster_type='affiliate',
            profile_image_url='profile_image_url',
            offline_image_url='offline_image_url',
            created_at=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        schema = TwichUserMapper.to_schema(entity)

        assert schema.id == entity.id
        assert schema.parsed_at == entity.parsed_at
