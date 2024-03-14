"""
common.py: File, containing common things related to queries.
"""


from typing import TypeVar
from application.queries.base import Query


Q = TypeVar('Q', bound=Query)
