"""
base.py: File, containing base twich parser interface.
"""


from abc import ABCMeta


class ITwichBaseParser(metaclass=ABCMeta):
    """
    ITwichBaseParser: Class, that represents base twich parser interface for all twich parsers.
    It contains common abstract methods for every twich parser.

    Args:
        ABCMeta: Base metaclass for base twich parser interface that make this class abstract.
    """

    pass
