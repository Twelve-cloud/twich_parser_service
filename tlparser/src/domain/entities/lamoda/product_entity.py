"""
product_entity.py: File, containing lamoda product entity.
"""


from datetime import datetime
from typing import Optional
from domain.entities.base.base_entity import BaseEntity


class LamodaProductEntity(BaseEntity):
    """
    LamodaProductEntity: Class, representing lamoda product entity.

    Args:
        BaseEntity (_type_): Base entity class.
    """

    def __init__(
        self,
        sku: Optional[str] = None,
        url: Optional[str] = None,
        category: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
        price_currency: Optional[str] = None,
        price_valid_until: Optional[datetime] = None,
        parsed_at: Optional[datetime] = None,
    ) -> None:
        """
        __init__: Initialize lamoda product entity

        Args:
            sku (Optional[str]): Sku of the product (it is ID of the product).
            url (Optional[str]): Url of the product.
            category (Optional[str]): Category of the product.
            description (Optional[str]): Description of the product.
            price (Optional[float]): Price of the product.
            price_currency (Optional[str]): Price currency of the product.
            price_valid_until (Optional[datetime]): Date until product price is valid.
            parsed_at (Optional[datetime]): Parsing date of the product.
        """

        super().__init__(parsed_at)

        self.sku = sku
        self.url = url
        self.category = category
        self.description = description
        self.price = price
        self.price_currency = price_currency
        self.price_valid_until = price_valid_until
