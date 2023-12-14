"""
lamoda_controllers.py: File, containing controllers for a lamoda app.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import Timeout, ConnectionError, RequestException, TooManyRedirects
from schemas.lamoda_schemas import LamodaProductSchema
from services.lamoda_services import LamodaService
from exceptions.lamoda_exceptions import WrongCategoryUrl


class LamodaController:
    """
    LamodaController: Class, that represents lamoda controller. It handles every http exception.
    """

    def __init__(self, lamoda_service: LamodaService) -> None:
        """
        __init__: Initialize lamoda controller class.

        Args:
            lamoda_service (LamodaService): LamodaService instance.
        """

        self.service = lamoda_service

    def parse_products(self, c: str) -> list[LamodaProductSchema]:
        """
        parse_products: Delegate parsing to LamodaService, catch and handle all exceptions.

        Args:
            c (str): Category lamoda url.

        Raises:
            HTTPException: Raised when client passed wrong category url.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[LamodaProductSchema]: List of LamodaProductSchema instances.
        """

        try:
            return self.service.parse_products(c)
        except WrongCategoryUrl:
            raise HTTPException(status_code=400, detail='Wrong category url')
        except ConnectionError:
            raise HTTPException(status_code=503, detail='Service unavaliable (connection issues)')
        except Timeout:
            raise HTTPException(status_code=503, detail='Service unavaliable (request timeout)')
        except TooManyRedirects:
            raise HTTPException(status_code=503, detail='Service unavaliable (too many redirects)')
        except RequestException:
            raise HTTPException(status_code=503, detail='Service unavaliable (requests error)')
        except ValidationError:
            raise HTTPException(status_code=400, detail='Validation error (parsing error)')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
