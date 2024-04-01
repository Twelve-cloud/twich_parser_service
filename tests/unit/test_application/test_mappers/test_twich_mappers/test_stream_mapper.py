"""
test_stream_mapper.py: File, containing tests for stream mapper.
"""


from datetime import datetime

from application.dtos.fastapi_schemas.twich.stream_schema import TwichStreamSchema
from application.mappers.twich.stream_mapper import TwichStreamMapper
from domain.entities.twich.stream_entity import TwichStreamEntity


class TestLamodaProductMapper:
    def test_to_domain(self):
        schema = TwichStreamSchema(
            id=1,
            user_id=1,
            user_name='user_name',
            user_login='user_login',
            game_id=1,
            game_name='game_name',
            language='language',
            title='title',
            tags=['tag1', 'tag2'],
            started_at=datetime.utcnow(),
            viewer_count=1,
            type='live',
            parsed_at=datetime.utcnow(),
        )

        entity = TwichStreamMapper.to_domain(schema)

        assert entity.id == schema.id
        assert entity.parsed_at == schema.parsed_at

    def test_to_schema(self):
        entity = TwichStreamEntity(
            id=1,
            user_id=1,
            user_name='user_name',
            user_login='user_login',
            game_id=1,
            game_name='game_name',
            language='language',
            title='title',
            tags=['tag1', 'tag2'],
            started_at=datetime.utcnow(),
            viewer_count=1,
            type='live',
            parsed_at=datetime.utcnow(),
        )

        schema = TwichStreamMapper.to_schema(entity)

        assert schema.id == entity.id
        assert schema.parsed_at == entity.parsed_at
