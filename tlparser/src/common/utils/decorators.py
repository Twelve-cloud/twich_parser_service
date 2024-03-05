"""
decorators.py: File, containing decorators.
"""


from typing import Any, Callable


def Singleton(aClass: Any) -> Callable:
    """
    Singleton: Decorator, that represents singleton design pattern.

    Args:
        aClass (Any): Any class.

    Returns:
        Callable: Wrapper class instance with overriden __call__ method.
    """

    class Wrapper:
        """
        Wrapper: Class, provide access to singleton instance.
        """

        instance: aClass = None

        def __call__(self, *args: tuple, **kwargs: dict) -> aClass:
            """
            __call__: Called when class with singleton decorator is being created.

            Returns:
                aClass: single aClass instance.
            """

            if self.instance is None:
                self.instance: aClass = aClass(*args, **kwargs)

            return self.instance

    return Wrapper()


class ReadOnlyClassProperty:
    """
    ReadOnlyClassProperty: Class, that provide read only class properties.
    """

    def __init__(self, function: Callable):
        """
        __init__: Initialize read only class property.

        Args:
            function (Callable): Function to decorate.
        """

        self.function: Callable = function

    def __get__(self, instance: Any, owner: Any) -> Any:
        """
        __get__: Called when property is accessed.

        Args:
            instance (Any): Class instance.
            owner (Any): Class object.

        Returns:
            Any: Value that function returns.
        """

        return self.function(owner)

    def __set__(self, instance: Any, value: Any) -> None:
        """
        __set__: Called when property is being set.

        Args:
            instance (Any): Class instance.
            value (Any): New value.

        Raises:
            AttributeError: Raised when __set__ is called.
        """

        raise AttributeError('Can not set value to read-only attribute')
