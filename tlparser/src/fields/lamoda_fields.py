"""
lamoda_types.py: File, containing types for lamoda parsing fields.
"""


from enum import Enum


class CurrencyType(str, Enum):
    """
    CurrencyType: Class, that represents type of the currency.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    byn: str = 'BYN'
    usd: str = 'USD'
    rub: str = 'RUB'
