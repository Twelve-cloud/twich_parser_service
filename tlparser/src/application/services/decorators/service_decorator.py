"""
service_decorator.py: File, containing service decorator.
"""


from common.interfaces import IDecorator, IExceptionHandler
from application.interfaces.services import IBaseService
from typing import Any


class ServiceDecorator(IDecorator):
    """
    ServiceDecorator: Class, that represents decorator for services.

    Args:
        IDecorator: Decorator interface.
    """

    def __init__(
        self,
        service: IBaseService,
        exception_handler: IExceptionHandler,
    ) -> None:
        """
        __init__: Initialize service decorator.

        Args:
            service (IBaseService): Service interface.
            exception_handler (IExceptionHandler): Exception handler interface.
        """

        self.service: IBaseService = service
        self.exception_handler: IExceptionHandler = exception_handler

    def __getattr__(self, name: str) -> Any:
        """
        __getattr__: Translate all calls to service.
        Also catch an exception and send it to handler exception.

        Args:
            name (str): Name of the attribute.

        Returns:
            Any: Any value that service returns.
        """

        try:
            return getattr(self.service, name)
        except Exception as exception:
            self.exception_handler.handle(exception)
