"""
lamoda_services.py: File, containing services for a lamoda app.
"""


from re import compile
from json import JSONDecodeError, loads
from bs4 import BeautifulSoup
from requests import Response, session
from config.lamoda_settings import settings
from schemas.lamoda_schemas import LamodaProductSchema
from repositories.irepositories import ILamodaRepository
from exceptions.lamoda_exceptions import WrongCategoryUrl


class LamodaService:
    """
    LamodaService: Class, that contains parsing logic for a lamoda app.
    """

    def __init__(self, lamoda_repository: ILamodaRepository) -> None:
        """
        __init__: Do some initialization for LamodaService class.

        Args:
            lamoda_repository (ILamodaRepository): Lamoda repository.
        """

        self.repositry = lamoda_repository

    def _prepare_product_links(self, c: str) -> list[str]:
        """
        _prepare_product_links: Parse lamoda category url and return list of product links.

        Args:
            c (str): Category lamoda url.

        Raises:
            WrongCategoryUrl: Raised when category url is wrong.

        Returns:
            list[str]: List of product links.
        """

        product_links: list[str] = []
        page: int = 1

        with session() as s:
            while True:
                response: Response = s.get(settings.LAMODA_CATEGORY_BASE_URL + c + f'?page={page}')
                soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
                tags: list = soup.find_all('a', href=compile('/p/'))

                if not tags and page == 1:
                    raise WrongCategoryUrl

                if not tags:
                    break

                product_links.extend([tag.attrs['href'] for tag in tags])
                page += 1

        return product_links

    def parse_products(self, c: str) -> list[LamodaProductSchema]:
        """
        parse_products: Parse lamoda products by category.

        Args:
            c (str): Category lamoda url.

        Returns:
            list[LamodaProductSchema]: List of LamodaProductSchema instances.
        """

        product_links: list[str] = self._prepare_product_links(c)
        products: list[LamodaProductSchema] = []

        with session() as s:
            for product_link in product_links:
                response: Response = s.get(settings.LAMODA_BASE_URL + product_link)
                soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
                product_data_text: str = soup.find_all('script')[-1].text.replace('&quot;', '')

                try:
                    product_data_json: dict = loads(product_data_text)[0]
                    product: dict = {
                        'sku': product_data_json['sku'],
                        'url': settings.LAMODA_BASE_URL + product_link,
                        'category': product_data_json['category'],
                        'description': product_data_json['description'],
                        'price': float(product_data_json['offers']['price']),
                        'price_currency': product_data_json['offers']['priceCurrency'],
                        'price_valid_until': product_data_json['offers']['priceValidUntil'],
                    }
                    products.append(LamodaProductSchema(**product))
                except (JSONDecodeError, KeyError):
                    pass

        # actions with repository

        return products
