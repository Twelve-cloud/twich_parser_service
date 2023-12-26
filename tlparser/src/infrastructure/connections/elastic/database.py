"""
database.py: File, containing elastic search database connection.
"""


from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections


class ElasticSearchDatabase:
    """
    ElasticSearchDatabase: Class, that represents connection with elastic search db.
    """

    def __init__(self, protocol: str, host: str, port: int) -> None:
        """
        __init__: Connect to elasticsearch database.

        Args:
            protocol (str): Database connection protocol.
            host (str): Database host.
            port (int): Database port.
        """

        self.connection: Elasticsearch = connections.create_connection(
            hosts=[f'{protocol}://{host}:{port}'],
            timeout=60,
        )
