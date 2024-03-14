"""
decorators.py: File, containing decorators.
"""


from typing import Any, Callable


def Singleton(aClass: Any) -> Callable:
    """
    Singleton: Decorator, that represents singleton design pattern.

    Args:
        aClass (Any): Any class that should be decorated.

    Returns:
        Callable: Wrapper class instance with overriden __call__ method.
    """

    class Wrapper:
        """
        Wrapper: Class, that provides access to singleton instance.
        """

        instance: aClass = None

        def __call__(self, *args: tuple, **kwargs: dict) -> aClass:
            """
            __call__: Called when class with singleton decorator is being created.

            Returns:
                aClass: Single aClass instance.
            """

            if self.instance is None:
                self.instance: aClass = aClass(*args, **kwargs)

            return self.instance

    return Wrapper()


class ReadOnlyClassProperty:
    """
    ReadOnlyClassProperty: Class, that provide read only class properties. It is a decorator.
    """

    def __init__(self, function: Callable):
        """
        __init__: Makes initialization.

        Args:
            function (Callable): Class method to decorate.
        """

        self.function: Callable = function

    def __get__(self, instance: Any, owner: Any) -> Any:
        """
        __get__: Called when property is being accessed.

        Args:
            instance (Any): Instance of the class.
            owner (Any): Class object itself.

        Returns:
            Any: Value that class method returns.
        """

        return self.function(owner)

    def __set__(self, instance: Any, value: Any) -> None:
        """
        __set__: Called when property is being set.

        Args:
            instance (Any): Instance of the class.
            owner (Any): Class object itself.

        Raises:
            AttributeError: Raised when __set__ is called to make property read-only.
        """

        raise AttributeError('Can not set value to read-only attribute')
