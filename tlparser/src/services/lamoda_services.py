"""
"""


from schemas.lamoda_schemas import LamodaProductSchema
from repositories.irepositories import ILamodaRepository


class LamodaService:
    def __init__(self, lamoda_repository: ILamodaRepository) -> None:
        self.repositry = lamoda_repository

    def parse_products(self, cat: str) -> list[LamodaProductSchema]:  # type: ignore
        print('in service')
