"""
parsing_consumer.py: File, containing consumer for parsing.
"""


from pickle import loads
from kafka import KafkaConsumer


class KafkaParsingConsumer:
    """
    KafkaParsingConsumer: Class, representing KafkaParsingConsumer.
    """

    def __init__(self, bootstrap_servers: str, api_version: tuple, topic: str) -> None:
        """
        __init__: Initialize kafka parsing consumer.

        Args:
            bootstrap_servers (str): Kafka host and port.
            api_version (tuple): Consumer api version.
            topic (str): Name of the topic.
        """

        self.consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            api_version=api_version,
            value_deserializer=lambda v: loads(v),
        )
        self.consumer.subscribe([topic])
