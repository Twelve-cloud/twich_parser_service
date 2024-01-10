"""
products_service.py: File, containing domain service for lamoda products.
"""


import asyncio
from datetime import datetime
from json import JSONDecodeError, loads
from math import ceil
from re import Match, compile, search
from typing import Optional
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from common.config.lamoda.settings import settings
from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.exceptions.lamoda.products_exceptions import WrongCategoryUrlException


class LamodaProductsDomainService:
    """
    LamodaProductsDomainService: Class, that contains business logic for lamoda products.
    """

    def __init__(self) -> None:
        """
        __init__: Do some initialization for LamodaProductsDomainService class.
        """

        pass

    async def _fetch_html(self, session: ClientSession, url: str) -> str:
        """
        _fetch_html: Returns html.

        Args:
            session (ClientSession): Aiohttp session.
            url (str): Url.

        Returns:
            tuple[str, str]: Html.
        """

        async with session.get(url) as response:
            html = await response.text()

        return html

    async def _prepare_product_links(
        self,
        session: ClientSession,
        category_url: str,
        product_count: int | float,
    ) -> list[str]:
        """
        _prepare_product_links: Return product links.

        Args:
            session (ClientSession): Aiohttp session.
            category_url (str): Category url.
            product_count (int | float): Number of products of certain category.

        Returns:
            list[str]: List of product links.
        """

        product_links: list[str] = []

        pages: int = int(ceil(product_count / 60))

        pending_category_page_requests: set[asyncio.Task] = {
            asyncio.create_task(self._fetch_html(session, category_url + f'?page={page}'))
            for page in range(1, pages + 1)
        }

        while pending_category_page_requests:
            done_category_page_requests, pending_category_page_requests = await asyncio.wait(
                pending_category_page_requests,
                return_when=asyncio.FIRST_COMPLETED,
            )

            for done_category_page_request in done_category_page_requests:
                category_page_html = await done_category_page_request
                soup: BeautifulSoup = BeautifulSoup(category_page_html, 'html.parser')
                tags: list = soup.find_all('a', href=compile('/p/'))
                product_links.extend([tag.attrs['href'] for tag in tags])

        return product_links

    async def parse_products(self, category_id: str) -> list[LamodaProductEntity]:
        """
        parse_products: Parse lamoda products by category.

        Args:
            category_id (str): Category lamoda identifier.

        Raises:
            WrongCategoryUrlException: Raised when url category is wrong.

        Returns:
            list[LamodaProductEntity]: List of LamodaProductEntity instances.
        """

        products: list[LamodaProductEntity] = []

        async with ClientSession() as session:
            category_url: str = settings.LAMODA_CATEGORY_BASE_URL + category_id

            async with session.get(category_url) as response:
                category_html: str = await response.text()

                target_category: Optional[Match] = search(
                    f'{{"id":{category_id}(.*?)}}',
                    category_html,
                )

                if target_category is None:
                    raise WrongCategoryUrlException

                product_count: int | float = loads(target_category.group(0)).get('found')

            product_links: list[str] = await self._prepare_product_links(
                session,
                settings.LAMODA_CATEGORY_BASE_URL + category_id,
                product_count,
            )

            pending_product_requests: set[asyncio.Task] = {
                asyncio.create_task(self._fetch_html(session, settings.LAMODA_BASE_URL + plink))
                for plink in product_links
            }

            while pending_product_requests:
                done_product_requests, pending_product_requests = await asyncio.wait(
                    pending_product_requests,
                    return_when=asyncio.FIRST_COMPLETED,
                )

                for done_products_request in done_product_requests:
                    product_html = await done_products_request
                    soup: BeautifulSoup = BeautifulSoup(product_html, 'html.parser')
                    product_data_text: str = soup.find_all('script')[-1].text.replace('&quot;', '')

                    try:
                        product_data_json: dict = loads(product_data_text)[0]
                        product_dict: dict = {
                            'sku': product_data_json['sku'],
                            'url': settings.LAMODA_BASE_URL + product_data_json['offers']['url'],
                            'category': product_data_json['category'],
                            'description': product_data_json['description'],
                            'price': float(product_data_json['offers']['price']),
                            'price_currency': product_data_json['offers']['priceCurrency'],
                            'price_valid_until': product_data_json['offers']['priceValidUntil'],
                        }
                        product_entity: LamodaProductEntity = LamodaProductEntity(**product_dict)
                        product_entity.price_valid_until = datetime.strptime(
                            product_dict['price_valid_until'][:-3],
                            '%Y-%m-%d %H:%M:%S.%f',
                        )
                        products.append(product_entity)
                    except (JSONDecodeError, KeyError):
                        pass

        return products
