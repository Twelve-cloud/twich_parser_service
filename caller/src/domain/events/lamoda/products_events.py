"""
products_events.py: File, containing lamoda products events.
"""


from dataclasses import dataclass
from domain.events.base.base_event import BaseDomainEvent


@dataclass
class PublicParseProductsCalledEvent(BaseDomainEvent):
    """
    PublicParseProductsCalledEvent: Represents that public parse endpoint's been called.

    Args:
        BaseDomainEvent (_type_): Base domain event abstract class.
    """

    category: str
