"""
test_stream_mapper.py: File, containing tests for stream mapper.
"""


from datetime import datetime
from domain.entities.twich.stream_entity import TwichStreamEntity
from infrastructure.mappers.twich.elastic.stream_mapper import TwichStreamMapper
from infrastructure.models.twich.elastic.stream_model import TwichStream


class TestLamodaProductMapper:
    def test_to_domain(self):
        persistence = TwichStream(
            id=1,
            user_id=1,
            user_name='user_name',
            user_login='user_login',
            game_id=1,
            game_name='game_name',
            language='language',
            title='title',
            tags=[{'tag': 'tag1'}, {'tag': 'tag2'}],
            started_at=datetime.utcnow(),
            viewer_count=1,
            type='live',
            parsed_at=datetime.utcnow(),
        )

        entity = TwichStreamMapper.to_domain(persistence)

        assert entity.id == persistence.id
        assert entity.parsed_at == persistence.parsed_at

    def test_to_persistence(self):
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

        persistence = TwichStreamMapper.to_persistence(entity)

        assert persistence.id == entity.id
        assert persistence.parsed_at == entity.parsed_at
