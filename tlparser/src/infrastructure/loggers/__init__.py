"""
__init__.py: File, containing other logger modules to simplify import.
"""


from common.loggers.stream_logger import StreamLogger


__all__: list[str] = [
    'StreamLogger',
]
