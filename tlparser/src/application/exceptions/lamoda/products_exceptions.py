"""
products_exceptions.py: File, containing exceptions for lamoda products.
"""


class WrongCategoryUrlException(Exception):
    """
    WrongCategoryUrlException: Class, that represents that category url is wrong.

    Args:
        Exception (_type_): Base superclass for WrongCategoryUrlException.
    """

    reasons: list[str] = [
        'Client specified wrong category url.',
    ]
