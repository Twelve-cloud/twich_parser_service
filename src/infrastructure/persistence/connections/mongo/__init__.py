"""
__init__.py: File, containing other connection modules to simplify import.
"""


from infrastructure.persistence.connections.mongo.connection import MongoConnection


__all__ = [
    'MongoConnection',
]
