"""
routes.py: File, containing routes for a endpoints of version 1.
"""


from fastapi import APIRouter
from config.settings import settings
from api.v1.endpoints.twich import router as twich_router
from api.v1.endpoints.lamoda import router as lamoda_router


routers: APIRouter = APIRouter()
router_list: list[APIRouter] = [twich_router, lamoda_router]


for router in router_list:
    routers.include_router(router, prefix=f'/{settings.API_VERSION}')
