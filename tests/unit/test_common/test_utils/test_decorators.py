"""
test_decorators.py: File, containing tests for decorators.
"""


import pytest
from common.utils.decorators import (
    ReadOnlyClassProperty,
    singleton,
)


class TestSingletonDecorator:
    def test_singlton_decorator(self):
        class SingletonTest:
            pass

        SingletonTest = singleton(SingletonTest)
        assert SingletonTest() is SingletonTest()


class TestReadOnlyClassProperty:
    def test_read_only_class_property(self):
        class ReadOnlyClassPropertyTest:
            def test(self):
                return []

            test = ReadOnlyClassProperty(test)

        assert ReadOnlyClassPropertyTest().test == []

        with pytest.raises(AttributeError):
            ReadOnlyClassPropertyTest().test = 1
