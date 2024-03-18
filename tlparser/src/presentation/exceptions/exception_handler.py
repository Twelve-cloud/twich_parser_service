"""
exception_handler.py: File, containing exception handler interface.
"""


from abc import ABCMeta, abstractmethod


class IExceptionHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, exception: Exception) -> None:
        pass
