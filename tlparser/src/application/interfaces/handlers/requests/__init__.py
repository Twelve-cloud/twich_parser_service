"""
__init__.py: File, containing other request handler modules to simplify import.
"""


from application.interfaces.handlers.requests.base import IBaseRequestHandler
from application.interfaces.handlers.requests.game import ITwichGameRequestHandler
from application.interfaces.handlers.requests.stream import ITwichStreamRequestHandler
from application.interfaces.handlers.requests.user import ITwichUserRequestHandler


__all__: list[str] = [
    'IBaseRequestHandler',
    'ITwichGameRequestHandler',
    'ITwichStreamRequestHandler',
    'ITwichUserRequestHandler',
]
