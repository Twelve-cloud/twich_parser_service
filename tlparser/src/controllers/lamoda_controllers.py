"""
lamoda_controllers.py: File, containing controllers for a lamoda app.
"""


from schemas.lamoda_schemas import LamodaProductSchema
from services.lamoda_services import LamodaService


class LamodaController:
    """
    LamodaController: Class, that represents lamoda controller. It handles every http exception.
    """

    def __init__(self, lamoda_service: LamodaService) -> None:
        self.service = lamoda_service

    def parse_products(self, cat: str) -> list[LamodaProductSchema]:  # type: ignore
        self.service.parse_products(cat)
