"""
decorators.py: File, containing decorators for a project.
"""


from typing import Any, Callable, Optional


def singleton(aClass: Any) -> Callable:
    """
    singleton: Decorator, that represents singleton design pattern.

    Args:
        aClass (Any): Any class.

    Returns:
        Callable: Wrapper function.
    """

    class Wrapper:
        """
        Wrapper: Class, provide access to singleton instance.

        Returns:
            _type_: Singleton instance.
        """

        instance: Optional[aClass] = None

        def __call__(self, *args: tuple, **kwargs: dict) -> Optional[aClass]:
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
        __init__: Do some initialization.

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
