"""
lamoda.py: File, containing endpoinds for a lamoda app.
"""


from typing import Annotated
from fastapi import Path, Depends, APIRouter, status
from core.containers import Container
from config.lamoda_metadata import parse_products_metadata
from schemas.lamoda_schemas import LamodaProductSchema
from dependency_injector.wiring import Provide, inject
from controllers.lamoda_controllers import LamodaController


router: APIRouter = APIRouter(
    prefix='/lamoda',
    tags=['lamoda'],
)


@router.post('/parse/products/{c:path}', status_code=status.HTTP_200_OK, **parse_products_metadata)
@inject
async def parse_products(
    c: Annotated[str, Path(min_length=1, max_length=128)],
    controller: LamodaController = Depends(Provide[Container.lamoda_controller]),
) -> list[LamodaProductSchema]:
    """
    parse_products: Parse lamoda products and return result as LamodaProductSchema.

    Args:
        c (str): Category of the products.
        controller (LamodaController): Lamoda controller.

    Returns:
        list[LamodaProductSchema]: Response as list of LamodaProductSchema instances.
    """

    return controller.parse_products(c)
