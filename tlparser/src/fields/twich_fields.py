"""
twich_types.py: File, containing types for twich parsing fields.
"""


from enum import Enum


class TwichUserType(str, Enum):
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


class TwichUserBroadcasterType(str, Enum):
    """
    TwichUserBroadcasterType: Class, that represents type of the broadcaster.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    affiliate: str = 'affiliate'
    partner: str = 'partner'
    normal: str = ''


class TwichStreamStatusType(str, Enum):
    """
    TwichStreamStatus: Class, that represents type of the stream status.

    Args:
        str (_type_): Base str superclass.
        Enum (_type_): Base enum superclass.
    """

    live: str = 'live'
