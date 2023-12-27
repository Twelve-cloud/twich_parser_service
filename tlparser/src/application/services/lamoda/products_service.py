"""
products_service.py: File, containing service for lamoda products.
"""


from json import JSONDecodeError, loads
from re import compile
from bs4 import BeautifulSoup
from requests import Response, session
from application.mappers.lamoda.product_mapper import (
    LamodaProductCreateMapper,
    LamodaProductReadMapper,
)
from application.schemas.lamoda.product_schema import (
    LamodaProductCreateSchema,
    LamodaProductReadSchema,
)
from common.config.lamoda.settings import settings
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.events.lamoda.products_events import (
    LamodaProductCreatedOrUpdatedEvent,
    LamodaProductsDeletedByCategoryEvent,
    PublicParseProductsCalledEvent,
)
from domain.exceptions.lamoda.products_exceptions import WrongCategoryUrlException
from domain.publishers.lamoda.products_publisher import LamodaProductsPublisher
from domain.repositories.base.base_repository import ResultWithEvent
from domain.repositories.lamoda.products_repository import LamodaProductsRepository


class LamodaProductsService:
    """
    LamodaProductsService: Class, that contains business logic for lamoda products.
    """

    def __init__(
        self,
        publisher: LamodaProductsPublisher,
        repository: LamodaProductsRepository,
    ) -> None:
        """
        __init__: Do some initialization for LamodaProductsService class.

        Args:
            repository (LamodaProductsRepository): Lamoda products repository.
        """

        self.repository: LamodaProductsRepository = repository
        self.publisher: LamodaProductsPublisher = publisher

    def _prepare_product_links(self, category: str) -> list[str]:
        """
        _prepare_product_links: Parse lamoda category url and return list of product links.

        Args:
            category (str): Category lamoda url.

        Raises:
            WrongCategoryUrl: Raised when category url is wrong.

        Returns:
            list[str]: List of product links.
        """

        product_links: list[str] = []
        page: int = 1

        with session() as s:
            category_url: str = settings.LAMODA_CATEGORY_BASE_URL + category

            while True:
                response: Response = s.get(category_url + f'?page={page}')
                soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
                tags: list = soup.find_all('a', href=compile('/p/'))

                if not tags and page == 1:
                    raise WrongCategoryUrlException

                if not tags:
                    break

                product_links.extend([tag.attrs['href'] for tag in tags])
                page += 1

        return product_links

    def parse_products(self, category: str) -> None:
        """
        parse_products: Called lamoda products publisher to publish event about parsing.

        Args:
            category (str): Category lamoda url.
        """

        event: PublicParseProductsCalledEvent = self.repository.parse_products(category)

        self.publisher.publish_parse_products_called_event(event)

        return

    def private_parse_products(self, category: str) -> list[LamodaProductReadSchema]:
        """
        private_parse_products: Parse lamoda products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductReadSchema]: List of LamodaProductReadSchema instances.
        """

        product_links: list[str] = self._prepare_product_links(category)
        products: list[LamodaProductReadSchema] = []

        with session() as s:
            for product_link in product_links:
                response: Response = s.get(settings.LAMODA_BASE_URL + product_link)
                soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
                product_data_text: str = soup.find_all('script')[-1].text.replace('&quot;', '')

                try:
                    product_data_json: dict = loads(product_data_text)[0]
                    product_dict: dict = {
                        'sku': product_data_json['sku'],
                        'url': settings.LAMODA_BASE_URL + product_link,
                        'category': product_data_json['category'],
                        'description': product_data_json['description'],
                        'price': float(product_data_json['offers']['price']),
                        'price_currency': product_data_json['offers']['priceCurrency'],
                        'price_valid_until': product_data_json['offers']['priceValidUntil'],
                    }

                    product_schema: LamodaProductCreateSchema = LamodaProductCreateSchema(
                        **product_dict
                    )

                    product: ResultWithEvent[
                        LamodaProductEntity, LamodaProductCreatedOrUpdatedEvent
                    ] = self.repository.create_or_update(
                        LamodaProductCreateMapper.to_domain(product_schema),
                    )

                    product_event: LamodaProductCreatedOrUpdatedEvent = product.event

                    self.publisher.publish_created_or_updated_event(product_event)

                    product_entity: LamodaProductEntity = product.result

                    products.append(LamodaProductReadMapper.to_schema(product_entity))
                except (JSONDecodeError, KeyError):
                    pass

        return products

    def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delete products by category.

        Args:
            category (str): Category lamoda url.
        """

        event: LamodaProductsDeletedByCategoryEvent = self.repository.delete_products_by_category(
            category,
        )

        self.publisher.publish_products_deleted_by_category_event(event)

        return

    def get_all_products(self) -> list[LamodaProductReadSchema]:
        """
        get_all_products: Return all products.

        Returns:
            list[LamodaProductReadSchema]: List of lamoda products.
        """

        return [
            LamodaProductReadMapper.to_schema(product_entity)
            for product_entity in self.repository.all()
        ]

    def get_products_by_category(self, category: str) -> list[LamodaProductReadSchema]:
        """
        get_products_by_category: Return products by category.

        Args:
            category (str): Category lamoda url.

        Returns:
            list[LamodaProductReadSchema]: List of lamoda products with the same category.
        """

        return [
            LamodaProductReadMapper.to_schema(product_entity)
            for product_entity in self.repository.get_products_by_category(category)
        ]
