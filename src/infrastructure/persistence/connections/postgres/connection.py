"""
connection.py: File, containing mongo database connection.
"""


from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


class PostgresConnection:
    def __init__(
        self,
        scheme: str,
        db_name: str,
        username: str,
        password: str,
        host: str,
        port: int,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            scheme
            + '://'
            + username
            + ':'
            + password
            + '@'
            + host
            + ':'
            + str(port)
            + '/'
            + db_name
        )
        self.async_sesion: sessionmaker = sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
