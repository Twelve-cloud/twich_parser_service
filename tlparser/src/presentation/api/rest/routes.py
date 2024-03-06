"""
routes.py: File, containing routes for a endpoints of version 1.
"""


from fastapi import APIRouter
from common.config import settings
from presentation.api.rest.v1.endpoints.game import router as game_router


# from presentation.api.rest.v1.endpoints.stream import router as stream_router
# from presentation.api.rest.v1.endpoints.user import router as user_router


routers: APIRouter = APIRouter()
router_list: list[APIRouter] = [game_router]  # user_router, stream_router]


for router in router_list:
    routers.include_router(router, prefix=f'/{settings.API_VERSION}')
