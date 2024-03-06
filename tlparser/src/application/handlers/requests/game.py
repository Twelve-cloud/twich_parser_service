"""
game.py: File, ...
"""


from application.interfaces.handlers.requests import ITwichGameRequestHandler
from application.interfaces.handlers.exceptions import IExceptionHandler
from application.interfaces.services import ITwichGameService
from application.dtos.requests import TwichGameRequest
from application.dtos.responses import TwichGameResponse


class TwichGameRequestHandler(ITwichGameRequestHandler):
    """
    TwichGameRequestHandler _summary_

    Args:
        ITwichGameRequestHandler (_type_): _description_
    """

    def __init__(self, service: ITwichGameService, exception_handler: IExceptionHandler) -> None:
        """
        __init__ _summary_

        Args:
            service (ITwichGameService): _description_
            exception_handler (IExceptionHandler): _description_
        """

        self.service: ITwichGameService = service
        self.exception_handler: IExceptionHandler = exception_handler
        self.handler_map = {

        }

    def handle(self, request: TwichGameRequest) -> TwichGameResponse:
        """
        handle _summary_

        Args:
            request (TwichGameRequest): _description_

        Returns:
            TwichGameResponse: _description_
        """

        try:
            handler = self.handler_map.get(type(request))

            if handler:
                handler(request)
        except Exception as exception:
            self.exception_handler.handle(exception)
