"""
main.py: File, containing main caller logic.
"""


from kafka import KafkaConsumer
from requests import get
from config.settings import settings
from consumer.parsing_consumer import KafkaParsingConsumer
from domain.events.lamoda.products_events import PublicParseProductsCalledEvent
from domain.events.twich.game_events import PublicParseGameCalledEvent
from domain.events.twich.stream_events import PublicParseStreamCalledEvent
from domain.events.twich.user_events import PublicParseUserCalledEvent


def main() -> None:
    """
    main: Consumer messages from kafka and call tlparser endpoints.
    """

    print('Caller has been started...')

    consumer: KafkaConsumer = KafkaParsingConsumer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_PARSING_TOPIC,
    ).consumer

    for event in consumer:
        match event.value.__class__.__name__:
            case PublicParseProductsCalledEvent.__name__:
                response = get(
                    f'{settings.TLPARSER_LAMODA_PRODUCTS_PARSE_URL}/{event.value.category}',
                    verify=False,
                )
                print(f'Status code: {response.status_code}, data {response.json()}')
            case PublicParseGameCalledEvent.__name__:
                response = get(
                    f'{settings.TLPARSER_TWICH_GAME_PARSE_URL}/{event.value.name}',
                    verify=False,
                )
                print(f'Status code: {response.status_code}, data {response.json()}')
            case PublicParseStreamCalledEvent.__name__:
                response = get(
                    f'{settings.TLPARSER_TWICH_STREAM_PARSE_URL}/{event.value.user_login}',
                    verify=False,
                )
                print(f'Status code: {response.status_code}, data {response.json()}')
            case PublicParseUserCalledEvent.__name__:
                response = get(
                    f'{settings.TLPARSER_TWICH_USER_PARSE_URL}/{event.value.login}',
                    verify=False,
                )
                print(f'Status code: {response.status_code}, data {response.json()}')
            case _:
                pass


main()
