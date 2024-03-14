"""
common.py: File, containing common things related to commands.
"""


from typing import TypeVar
from application.commands.base import Command


C = TypeVar('C', bound=Command)
