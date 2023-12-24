"""
producer.py, File, containing kafka producer.
"""


import pickle
from kafka import KafkaProducer


class KafkaProducerConnection:
    """
    KafkaProducer: Class, that represents connection to kafka cluster.
    """

    def __init__(self, bootstrap_servers: str):
        """
        __init__: Initialize kafka producer.

        Args:
            bootstrap_servers (str): connection host and port.
        """

        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: pickle.dumps(v),
        )
