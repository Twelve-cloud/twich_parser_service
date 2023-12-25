"""
producer.py, File, containing kafka producer.
"""


from pickle import dumps
from kafka import KafkaProducer


class KafkaProducerConnection:
    """
    KafkaProducer: Class, that represents connection to kafka cluster.
    """

    def __init__(self, bootstrap_servers: str, api_version: str):
        """
        __init__: Initialize kafka producer.

        Args:
            bootstrap_servers (str): connection host and port.
        """

        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_serializer=lambda v: dumps(v),
        )
