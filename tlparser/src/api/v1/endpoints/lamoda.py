"""
lamoda.py: File, containing endpoinds for a lamoda app.
"""


from fastapi import Depends, APIRouter, status
from core.containers import Container
from config.lamoda_metadata import parse_products_metadata
from schemas.lamoda_schemas import LamodaProductSchema
from dependency_injector.wiring import Provide, inject
from controllers.lamoda_controllers import LamodaController


router: APIRouter = APIRouter(
    prefix='/lamoda',
    tags=['lamoda'],
)


@router.post('/parse/products/{cat}', status_code=status.HTTP_200_OK, **parse_products_metadata)
@inject
async def parse_products(
    cat: str, controller: LamodaController = Depends(Provide[Container.lamoda_controller])
) -> list[LamodaProductSchema]:
    """
    parse_products: Parse lamoda products and return result as LamodaProductSchema.

    Args:
        category (str): Category of the products.
        controller (LamodaController): Lamoda controller.

    Returns:
        list[LamodaProductSchema]: Response as list of LamodaProductSchema instances.
    """

    return controller.parse_products(cat)
