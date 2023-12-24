"""
products.py: File, containing endpoinds for lamoda products.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from application.schemas.lamoda.product_schema import LamodaProductReadSchema
from container import Container
from presentation.api.v1.endpoints.metadata.lamoda.products_metadata import LamodaProductsMetadata
from presentation.controllers.lamoda.products_controller import LamodaProductsController


router: APIRouter = APIRouter(
    prefix='/lamoda',
    tags=['lamoda'],
)


@router.post(
    path='/products/{category:path}',
    status_code=status.HTTP_200_OK,
    **LamodaProductsMetadata.parse_products,
)
@inject
async def parse_products(
    category: Annotated[str, Path(min_length=1, max_length=128)],
    controller: LamodaProductsController = Depends(Provide[Container.lamoda_products_w_controller]),
) -> Response:
    """
    parse_products: Produce message of parsing products to kafka.

    Args:
        category (str): Category of the products.

    Returns:
        Response: HTTP status code 200.
    """

    controller.parse_products(category)

    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


@router.get(
    path='/private/products/{category:path}',
    status_code=status.HTTP_200_OK,
    **LamodaProductsMetadata.private_parse_products,
)
@cache(expire=60)
@inject
async def private_parse_products(
    category: Annotated[str, Path(min_length=1, max_length=128)],
    controller: LamodaProductsController = Depends(Provide[Container.lamoda_products_w_controller]),
) -> list[LamodaProductReadSchema]:
    """
    private_parse_products: Parse lamoda products and return result as LamodaProductReadSchema.

    Args:
        category (str): Category of the products.
        controller (LamodaProductsController): Lamoda controller.

    Returns:
        list[LamodaProductReadSchema]: Response as list of LamodaProductReadSchema instances.
    """

    return controller.private_parse_products(category)


@router.delete(
    path='/products/{category:path}',
    status_code=status.HTTP_204_NO_CONTENT,
    **LamodaProductsMetadata.delete_products_by_category,
)
@inject
async def delete_products_by_category(
    category: Annotated[str, Path(min_length=1, max_length=128)],
    controller: LamodaProductsController = Depends(Provide[Container.lamoda_products_w_controller]),
) -> Response:
    """
    delete_products_by_category: Delete lamoda products by category.

    Args:
        category (str): Category of the products.
        controller (LamodaProductsController): Lamoda controller.

    Returns:
        Response: HTTP status code 204.
    """

    controller.delete_products_by_category(category)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    path='/products',
    status_code=status.HTTP_200_OK,
    **LamodaProductsMetadata.get_all_products,
)
@cache(expire=60)
@inject
async def get_all_products(
    controller: LamodaProductsController = Depends(Provide[Container.lamoda_products_r_controller]),
) -> list[LamodaProductReadSchema]:
    """
    get_all_products: Return all lamoda products.

    Args:
        controller (LamodaProductsController): Lamoda controller.

    Returns:
        list[LamodaProductReadSchema]: List of lamoda products.
    """

    return controller.get_all_products()


@router.get(
    path='/products/{category:path}',
    status_code=status.HTTP_200_OK,
    **LamodaProductsMetadata.get_products_by_category,
)
@cache(expire=60)
@inject
async def get_products_by_category(
    category: Annotated[str, Path(min_length=1, max_length=128)],
    controller: LamodaProductsController = Depends(Provide[Container.lamoda_products_r_controller]),
) -> list[LamodaProductReadSchema]:
    """
    get_products_by_category: Return lamoda products with the same category.

    Args:
        category (str): Category of the products.
        controller (LamodaProductsController): Lamoda controller.

    Returns:
        list[LamodaProductReadSchema]: List of lamoda products with the same category.
    """

    return controller.get_products_by_category(category)
