"""
__init__.py: File, containing other dependency modules to simplify import.
"""


from infrastructure.parsers.aiohttp.dependencies.common import TwichAPIToken, get_twich_api_token


__all__: list[str] = [
    'TwichAPIToken',
    'get_twich_api_token',
]
