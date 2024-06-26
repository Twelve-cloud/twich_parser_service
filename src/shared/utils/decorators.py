"""
decorators.py: File, containing decorators.
"""


from typing import (
    Any,
    Callable,
)


def Singleton(aClass: Any) -> Callable:
    class Wrapper:
        instance: aClass = None

        def __call__(self, *args: tuple, **kwargs: dict) -> aClass:
            if self.instance is None:
                self.instance: aClass = aClass(*args, **kwargs)

            return self.instance

    return Wrapper()


class ReadOnlyClassProperty:
    def __init__(self, function: Callable):
        self.function: Callable = function

    def __get__(self, instance: Any, owner: Any) -> Any:
        return self.function(owner)

    def __set__(self, instance: Any, value: Any) -> None:
        raise AttributeError('Can not set value to read-only attribute')
