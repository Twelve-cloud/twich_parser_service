"""
lamoda_exceptions.py: File, containing exceptions for a lamoda app.
"""


class WrongCategoryUrl(Exception):
    """
    WrongCategoryUrl: Class, that represents that category url is wrong.

    Args:
        Exception (_type_): Base superclass for WrongCategoryUrl.
    """

    reasons: list[str] = [
        'Client specified wrong category url.',
    ]
