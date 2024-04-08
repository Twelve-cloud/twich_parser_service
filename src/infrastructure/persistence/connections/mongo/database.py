"""
database.py: File, containing mongo database connection.
"""


from mongoengine import connect
from pymongo import MongoClient


class MongoDatabase:
    """
    MongoDatabase: Class, that represents connection with mongo db.
    """

    def __init__(
        self,
        db_name: str,
        username: str,
        password: str,
        host: str,
        port: int,
        authentication_source: str,
    ) -> None:
        """
        __init__: Connect to mongo database.

        Args:
            db_name (str): Name of the database.
            username (str): Name of the user of the database.
            password (str): Password of the database.
            host (str): Database host.
            port (int): Database port.
            authentication_source (str): The database to authentificate on.
        """

        self.connection: MongoClient = connect(
            db_name,
            username=username,
            password=password,
            host=host,
            port=port,
            authentication_source=authentication_source,
        )
