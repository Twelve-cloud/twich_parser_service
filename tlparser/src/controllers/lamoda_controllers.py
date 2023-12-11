"""
lamoda_controllers.py: File, containing controllers for a lamoda app.
"""


from schemas.lamoda_schemas import LamodaProductSchema


class LamodaController:
    """
    LamodaController: Class, that represents lamoda controller. It handles every http exception.
    """

    async def parse_products(self, cat: str) -> list[LamodaProductSchema]:  # type: ignore
        pass
