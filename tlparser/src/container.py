"""
container.py: File, containing container that describe all dependencies in the project.
"""


from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from dependency_injector.providers import (
    Factory,
    Resource,
    Singleton,
)
from application.handlers.command import (
    DeleteTwichGameHandler,
    ParseTwichGameHandler,
    DeleteTwichStreamHandler,
    ParseTwichStreamHandler,
    DeleteTwichUserHandler,
    ParseTwichUserHandler,
)
from application.handlers.query import (
    GetAllTwichGamesHandler,
    GetTwichGameByNameHandler,
    GetAllTwichStreamsHandler,
    GetTwichStreamByUserLoginHandler,
    GetAllTwichUsersHandler,
    GetTwichUserByLoginHandler,
)
from shared.config import settings
from infrastructure.buses.command import InMemoryCommandBus
from infrastructure.buses.query import InMemoryQueryBus
from infrastructure.loggers.logging import StreamLogger
from infrastructure.parsers.aiohttp import (
    TwichGameParser,
    TwichStreamParser,
    TwichUserParser,
)
from infrastructure.parsers.aiohttp.dependencies import get_twich_api_token
# change below
from infrastructure.persistence.connections.elastic.database import ElasticSearchDatabase
from infrastructure.persistence.connections.mongo.database import MongoDatabase
from infrastructure.persistence.repositories.elastic.game import TwichGameElasticRepository
from infrastructure.persistence.repositories.elastic.stream import TwichStreamElasticRepository
from infrastructure.persistence.repositories.elastic.user import TwichUserElasticRepository
from infrastructure.persistence.repositories.mongo.game import TwichGameMongoRepository
from infrastructure.persistence.repositories.mongo.stream import TwichStreamMongoRepository
from infrastructure.persistence.repositories.mongo.user import TwichUserMongoRepository
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection
from infrastructure.publishers.kafka.game import TwichGameKafkaPublisher
from infrastructure.publishers.kafka.stream import TwichStreamKafkaPublisher
from infrastructure.publishers.kafka.user import TwichUserKafkaPublisher
from presentation.dispatchers.kafka.game import TwichGameKafkaDispatcher
from presentation.dispatchers.kafka.stream import TwichStreamKafkaDispatcher
from presentation.dispatchers.kafka.user import TwichUserKafkaDispatcher
from presentation.api.rest.v1.controllers.game import TwichGameController, TwichGameReadController


class Container(DeclarativeContainer):
    """
    Container: Class, that describe all dependencies in the project.

    Args:
        DeclarativeContainer (_type_): Base superclass for a Container class.
    """

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            'presentation.api.rest.v1.controllers.game',
            # 'presentation.api.rest.v1.endpoints.user',
            # 'presentation.api.rest.v1.endpoints.stream',
            # 'presentation.api.graphql.queries.twich.game_queries',
            # 'presentation.api.graphql.mutations.twich.game_mutations',
        ],
    )

    # ------------------------------------- Dependencies ------------------------------------------

    twich_api_token: Resource = Resource(
        get_twich_api_token,
    )

    # ------------------------------------- Parsers ---------------------------------------

    twich_game_parser: Factory = Factory(
        TwichGameParser,
        token=twich_api_token,
    )

    twich_user_parser: Factory = Factory(
        TwichUserParser,
        token=twich_api_token,
    )

    twich_stream_parser: Factory = Factory(
        TwichStreamParser,
        token=twich_api_token,
    )

    # ------------------------------------- Kafka -------------------------------------------------

    kafka_producer: Singleton = Singleton(
        KafkaProducerConnection,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_PRODUCER_API_VERSION,
    )

    # ---------------------------------- Publishers ------------------------------------------------

    twich_game_kafka_publisher: Factory = Factory(
        TwichGameKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    twich_user_kafka_publisher: Factory = Factory(
        TwichUserKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    twich_stream_kafka_publisher: Factory = Factory(
        TwichStreamKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    # ------------------------------------ Databases ----------------------------------------------

    mongo: Singleton = Singleton(
        MongoDatabase,
        db_name=settings.DB_MONGO_NAME,
        username=settings.DB_MONGO_USERNAME,
        password=settings.DB_MONGO_PASSWORD,
        host=settings.DB_MONGO_HOST,
        port=settings.DB_MONGO_PORT,
        authentication_source=settings.DB_MONGO_AUTH_SOURCE,
    )

    elastic: Singleton = Singleton(
        ElasticSearchDatabase,
        protocol=settings.ELASTIC_PROTOCOL,
        host=settings.ELASTIC_HOST,
        port=settings.ELASTIC_PORT,
    )

    # ---------------------------------- Repositories ----------------------------------------------

    twich_game_mongo_repository: Factory = Factory(
        TwichGameMongoRepository,
        db=mongo,
    )

    twich_user_mongo_repository: Factory = Factory(
        TwichUserMongoRepository,
        db=mongo,
    )

    twich_stream_mongo_repository: Factory = Factory(
        TwichStreamMongoRepository,
        db=mongo,
    )

    twich_game_elastic_repository: Factory = Factory(
        TwichGameElasticRepository,
        db=elastic,
    )

    twich_user_elastic_repository: Factory = Factory(
        TwichUserElasticRepository,
        db=elastic,
    )

    twich_stream_elastic_repository: Factory = Factory(
        TwichStreamElasticRepository,
        db=elastic,
    )

    # ----------------------------------- Command Handlers ----------------------------------------

    parse_game_handler: Factory = Factory(
        ParseTwichGameHandler,
        parser=twich_game_parser,
        repository=twich_game_mongo_repository,
        publisher=twich_game_kafka_publisher,
    )

    delete_game_handler: Factory = Factory(
        DeleteTwichGameHandler,
        repository=twich_game_elastic_repository,
        publisher=twich_game_kafka_publisher,
    )

    parse_stream_handler: Factory = Factory(
        ParseTwichStreamHandler,
        parser=twich_user_parser,
        repository=twich_user_mongo_repository,
        publisher=twich_user_kafka_publisher,
    )

    delete_stream_handler: Factory = Factory(
        DeleteTwichStreamHandler,
        repository=twich_user_elastic_repository,
        publisher=twich_user_kafka_publisher,
    )

    parse_user_handler: Factory = Factory(
        ParseTwichUserHandler,
        parser=twich_stream_parser,
        repository=twich_stream_mongo_repository,
        publisher=twich_stream_kafka_publisher,
    )

    delete_user_handler: Factory = Factory(
        DeleteTwichUserHandler,
        repository=twich_stream_elastic_repository,
        publisher=twich_stream_kafka_publisher,
    )

    # ----------------------------------- Query handlers -------------------------------------------

    get_all_games_handler: Factory = Factory(
        GetAllTwichGamesHandler,
        repository=twich_game_mongo_repository,
    )

    get_twich_game_by_name_handler: Factory = Factory(
        GetTwichGameByNameHandler,
        repository=twich_game_elastic_repository,
    )

    get_all_twich_streams_handler: Factory = Factory(
        GetAllTwichStreamsHandler,
        repository=twich_user_mongo_repository,
    )

    twich_twich_stream_by_user_login_handler: Factory = Factory(
        GetTwichStreamByUserLoginHandler,
        repository=twich_user_elastic_repository,
    )

    get_all_twich_users_handler: Factory = Factory(
        GetAllTwichUsersHandler,
        repository=twich_stream_mongo_repository,
    )

    get_twich_user_by_login_handler: Factory = Factory(
        GetTwichUserByLoginHandler,
        repository=twich_stream_elastic_repository,
    )

    # --------------------------------- Buses ------------------------------------------------------

    in_memory_command_bus: Factory = Factory(
        InMemoryCommandBus,
    )

    in_memory_query_bus: Factory = Factory(
        InMemoryQueryBus,
    )

    # --------------------------------- Dispatchers ------------------------------------------------

    twich_game_kafka_dispatcher: Singleton = Singleton(
        TwichGameKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_GAME_TOPIC,
        repository=twich_game_elastic_repository,
    )

    twich_user_kafka_dispatcher: Singleton = Singleton(
        TwichUserKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_USER_TOPIC,
        repository=twich_user_elastic_repository,
    )

    twich_stream_kafka_dispatcher: Singleton = Singleton(
        TwichStreamKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_STREAM_TOPIC,
        repository=twich_stream_elastic_repository,
    )

    # ---------------------------------- Loggers ---------------------------------------------------

    logger: Factory = Factory(
        StreamLogger,
    )

    # ------------------------------- Controllers --------------------------------------------------

    twich_game_controller: Factory = Factory(
        TwichGameController,
        command_bus=in_memory_command_bus,
    )

    twich_game_read_controller: Factory = Factory(
        TwichGameReadController,
        query_bus=in_memory_query_bus,
    )
