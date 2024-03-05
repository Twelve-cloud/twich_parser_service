"""
__init__.py: File, containing other decorator modules to simplify import.
"""


from application.services.decorators.service_decorator import ServiceDecorator


__all__: list[str] = [
    'ServiceDecorator',
]
