"""
test_product_mapper.py: File, containing tests for product mapper.
"""


from datetime import datetime
from application.dtos.fastapi_schemas.lamoda.product_schema import LamodaProductSchema
from application.mappers.lamoda.product_mapper import LamodaProductMapper
from domain.entities.lamoda.product_entity import LamodaProduct


class TestLamodaProductMapper:
    def test_to_domain(self):
        schema = LamodaProductSchema(
            sku='sku',
            url='url',
            category='category',
            description='description',
            price=0.0,
            price_currency='BYN',
            price_valid_until=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        entity = LamodaProductMapper.to_domain(schema)

        assert entity.sku == schema.sku
        assert entity.parsed_at == schema.parsed_at

    def test_to_schema(self):
        entity = LamodaProduct(
            sku='sku',
            url='url',
            category='category',
            description='description',
            price=0.0,
            price_currency='BYN',
            price_valid_until=datetime.utcnow(),
            parsed_at=datetime.utcnow(),
        )

        schema = LamodaProductMapper.to_schema(entity)

        assert schema.sku == entity.sku
        assert schema.parsed_at == entity.parsed_at
