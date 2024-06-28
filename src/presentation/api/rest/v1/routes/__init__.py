"""
__init__.py: File, containing other routes modules to simplify import.
"""


from fastapi import APIRouter

from presentation.api.rest.v1.routes.game import router as game_router
from presentation.api.rest.v1.routes.stream import router as stream_router
from presentation.api.rest.v1.routes.user import router as user_router


rest_router: APIRouter = APIRouter(
    prefix='/v1',
)

for router in [game_router, stream_router, user_router]:
    rest_router.include_router(router)


__all__: list[str] = [
    'rest_router',
]
