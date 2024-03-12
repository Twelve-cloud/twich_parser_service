"""
__init__.py: File, containing other command handler modules to simplify import.
"""


from application.handlers.game import (
    DeleteTwichGameCommandHandler,
    ParseTwichGameCommandHandler,
)
from application.handlers.stream import (
    DeleteTwichStreamCommandHandler,
    ParseTwichStreamCommandHandler,
)
from application.handlers.user import (
    DeleteTwichUserCommandHandler,
    ParseTwichUserCommandHandler,
)


__all__: list[str] = [
    'DeleteTwichGameCommandHandler',
    'ParseTwichGameCommandHandler',
    'DeleteTwichStreamCommandHandler',
    'ParseTwichStreamCommandHandler',
    'DeleteTwichUserCommandHandler',
    'ParseTwichUserCommandHandler',
]
