"""
meta_fields.py: File, containing metaclasses for enums for a project.
"""


from enum import EnumMeta
from typing import Any, ClassVar


class ReadOnlyChoicesDescriptor:
    """
    ReadOnlyChoicesDescriptor: Class descriptor, that provides special logic for attributes.
    """

    def __get__(self, instance: Any, owner: Any) -> list[tuple]:
        """
        __get__: Called when property is accessed.

        Args:
            instance (Any): Class instance.
            owner (Any): Class object.

        Returns:
            list[tuple]: List of tuples.
        """

        return [item.value for item in instance]

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


class EnumMetaclass(EnumMeta):
    """
    EnumMetaclass: Metaclass for every enum in a project.

    Args:
        EnumMeta (_type_): Base metaclass for each Enum class and subclasses.
    """

    choices: ClassVar[ReadOnlyChoicesDescriptor] = ReadOnlyChoicesDescriptor()
