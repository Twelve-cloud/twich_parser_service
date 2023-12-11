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
                self.instance = aClass(*args, **kwargs)

            return self.instance

    return Wrapper()
