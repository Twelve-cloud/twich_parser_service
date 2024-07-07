"""
__init__.py: File, containing other connection modules to simplify import.
"""


from infrastructure.persistence.connections.postgres.connection import PostgresConnection


__all__ = [
    'PostgresConnection',
]
