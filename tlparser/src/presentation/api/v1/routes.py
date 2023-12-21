"""
routes.py: File, containing routes for a endpoints of version 1.
"""


from fastapi import APIRouter
from common.config.base.settings import settings
from presentation.api.v1.endpoints.rest.lamoda.products import router as products_router
from presentation.api.v1.endpoints.rest.twich.game import router as game_router
from presentation.api.v1.endpoints.rest.twich.stream import router as stream_router
from presentation.api.v1.endpoints.rest.twich.user import router as user_router


routers: APIRouter = APIRouter()
router_list: list[APIRouter] = [products_router, game_router, user_router, stream_router]


for router in router_list:
    routers.include_router(router, prefix=f'/{settings.API_VERSION}')
