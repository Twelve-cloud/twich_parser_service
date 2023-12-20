"""
user_fields.py: File, containing types for twich user.
"""


from enum import Enum
from application.fields.base.meta_fields import EnumMetaclass


class TwichUserType(str, Enum, metaclass=EnumMetaclass):
    """
    TwichUserType: Class, that represents type of the user.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    admin: str = 'admin'
    staff: str = 'staff'
    global_mod: str = 'global_mode'
    user: str = ''


class TwichUserBroadcasterType(str, Enum, metaclass=EnumMetaclass):
    """
    TwichUserBroadcasterType: Class, that represents type of the broadcaster.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    affiliate: str = 'affiliate'
    partner: str = 'partner'
    normal: str = ''
