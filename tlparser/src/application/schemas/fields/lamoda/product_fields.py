"""
product_fields.py: File, containing types for lamoda product.
"""


from enum import Enum
from application.schemas.fields.base.meta_fields import EnumMetaclass


class CurrencyType(str, Enum, metaclass=EnumMetaclass):
    """
    CurrencyType: Class, that represents type of the currency.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    byn: str = 'BYN'
    usd: str = 'USD'
    rub: str = 'RUB'
