"""
__init__.py: File, containing other service modules to simplify import.
"""


from application.interfaces.services.base import IBaseService
from application.interfaces.services.game import ITwichGameService
from application.interfaces.services.stream import ITwichStreamService
from application.interfaces.services.user import ITwichUserService


__all__: list[str] = [
    'IBaseService',
    'ITwichGameService',
    'ITwichStreamService',
    'ITwichUserService',
]
