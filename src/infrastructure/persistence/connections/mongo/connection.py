"""
connection.py: File, containing mongo database connection.
"""


from mongoengine import connect
from pymongo import MongoClient


class MongoConnection:
    def __init__(
        self,
        db_name: str,
        username: str,
        password: str,
        host: str,
        port: int,
        authentication_source: str,
    ) -> None:
        self.connection: MongoClient = connect(
            db_name,
            username=username,
            password=password,
            host=host,
            port=port,
            authentication_source=authentication_source,
        )
