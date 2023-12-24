"""
products_events.py: File, containing lamoda products events.
"""


from dataclasses import dataclass
from datetime import datetime
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseProductsCalledEvent(BaseDomainEvent):
    """
    PublicParseProductsCalledEvent: Represents that public parse endpoint's been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    type: str
    category: str


@dataclass
class LamodaProductCreatedOrUpdatedEvent(BaseDomainEvent):
    """
    LamodaProductCreatedOrUpdatedEvent: Represents that products've been created/updated.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    sku: str
    url: str
    category: str
    description: str
    price: float
    price_currency: str
    price_valid_until: datetime
    parsed_at: datetime


@dataclass
class LamodaProductsDeletedByCategoryEvent(BaseDomainEvent):
    """
    LamodaProductsDeletedByCategoryEvent: Represents that products've been deleted by category.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    category: str
