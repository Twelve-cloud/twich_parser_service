"""
exception_handler.py: File, containing exception handler interface.
"""


from abc import ABCMeta, abstractmethod


class IExceptionHandler(metaclass=ABCMeta):
    """
    IExceptionHandler: Class, that represents exception handler interface.

    Args:
        ABCMeta: Base metaclass for exception handler interface that make this class abstract.
    """

    @abstractmethod
    def handle(self, exception: Exception) -> None:
        """
        handle: Should handle exceptions.
        Must be overriden.

        Args:
            exception (Exception): Exception that should be handled.
        """

        pass
