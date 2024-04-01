"""
__init__.py: File, containing other controller modules to simplify import.
"""


from presentation.api.rest.v1.controllers.game import (
    TwichGameCommandController,
    TwichGameQueryController,
)
from presentation.api.rest.v1.controllers.stream import (
    TwichStreamCommandController,
    TwichStreamQueryController,
)
from presentation.api.rest.v1.controllers.user import (
    TwichUserCommandController,
    TwichUserQueryController,
)


__all__: list[str] = [
    'TwichGameCommandController',
    'TwichGameQueryController',
    'TwichStreamCommandController',
    'TwichStreamQueryController',
    'TwichUserCommandController',
    'TwichUserQueryController',
]
