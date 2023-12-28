"""
stream_fields.py: File, containing types for twich stream.
"""


from enum import Enum
from application.schemas.fields.base.meta_fields import EnumMetaclass


class TwichStreamStatusType(str, Enum, metaclass=EnumMetaclass):
    """
    TwichStreamStatusType: Class, that represents type of the stream status.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    live: str = 'live'
