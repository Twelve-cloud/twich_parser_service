"""
container.py: File, containing container that describe all dependencies in the project.
"""


from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from dependency_injector.providers import (
    Container,
    Dependency,
    Dict,
    Factory,
    Resource,
    Singleton,
)

from application.commands import (
    DeleteTwichGame,
    DeleteTwichGameByName,
    DeleteTwichStream,
    DeleteTwichStreamByUserLogin,
    DeleteTwichUser,
    DeleteTwichUserByLogin,
    ParseTwichGame,
    ParseTwichStream,
    ParseTwichUser,
)
from application.exceptions import (
    ObjectNotFoundException,
    ParserException,
    TwichGetObjectBadRequestException,
    TwichRequestTimeoutException,
    TwichRequestUnauthorizedException,
    TwichTokenNotObtainedException,
)
from application.handlers.command import (
    DeleteTwichGameByNameHandler,
    DeleteTwichGameHandler,
    DeleteTwichStreamByUserLoginHandler,
    DeleteTwichStreamHandler,
    DeleteTwichUserByLoginHandler,
    DeleteTwichUserHandler,
    ExceptionHandlingDecorator as CExceptionHandlingDecorator,
    ParseTwichGameHandler,
    ParseTwichStreamHandler,
    ParseTwichUserHandler,
)
from application.handlers.exception import (
    ObjectNotFoundExceptionHandler,
    ParserExceptionHandler,
    TwichGetObjectBadRequestExceptionHandler,
    TwichRequestTimeoutExceptionHandler,
    TwichRequestUnauthorizedExceptionHandler,
    TwichTokenNotObtainedExceptionHandler,
)
from application.handlers.query import (
    ExceptionHandlingDecorator as QExceptionHandlingDecorator,
    GetAllTwichGamesHandler,
    GetAllTwichStreamsHandler,
    GetAllTwichUsersHandler,
    GetTwichGameByNameHandler,
    GetTwichGameHandler,
    GetTwichStreamByUserLoginHandler,
    GetTwichStreamHandler,
    GetTwichUserByLoginHandler,
    GetTwichUserHandler,
)
from application.queries import (
    GetAllTwichGames,
    GetAllTwichStreams,
    GetAllTwichUsers,
    GetTwichGame,
    GetTwichGameByName,
    GetTwichStream,
    GetTwichStreamByUserLogin,
    GetTwichUser,
    GetTwichUserByLogin,
)
from infrastructure.buses.command import InMemoryCommandBus
from infrastructure.buses.query import InMemoryQueryBus
from infrastructure.loggers.logging import StreamLogger
from infrastructure.parsers.aiohttp import (
    TwichGameParser,
    TwichStreamParser,
    TwichUserParser,
)
from infrastructure.parsers.aiohttp.dependencies import get_twich_api_token
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
from presentation.api.rest.v1.controllers import (
    ControllerExceptionHandlingDecorator,
    TwichGameCommandController,
    TwichGameQueryController,
    TwichStreamCommandController,
    TwichStreamQueryController,
    TwichUserCommandController,
    TwichUserQueryController,
)
from presentation.api.rest.v1.handlers.exception import (
    ObjectNotFoundExceptionHandler as RestObjectNotFoundExceptionHandler,
    ParserExceptionHandler as RestParserExceptionHandler,
    TwichGetObjectBadRequestExceptionHandler as RestTwichGetObjectBadRequestExceptionHandler,
    TwichRequestTimeoutExceptionHandler as RestTwichRequestTimeoutExceptionHandler,
    TwichRequestUnauthorizedExceptionHandler as RestTwichRequestUnauthorizedExceptionHandler,
    TwichTokenNotObtainedExceptionHandler as RestTwichTokenNotObtainedExceptionHandler,
)
from presentation.dispatchers.kafka.game import TwichGameKafkaDispatcher
from presentation.dispatchers.kafka.stream import TwichStreamKafkaDispatcher
from presentation.dispatchers.kafka.user import TwichUserKafkaDispatcher
from shared.config import settings


class TwichGameContainer(DeclarativeContainer):
    # ---------------- change ------------------------

    twich_api_token: Dependency = Dependency()
    kafka_producer: Dependency = Dependency()
    mongo: Dependency = Dependency()
    elastic: Dependency = Dependency()
    logger: Dependency = Dependency()
    command_exception_handlers: Dependency = Dependency()
    query_exception_handlers: Dependency = Dependency()
    rest_v1_controller_exception_handlers: Dependency = Dependency()

    game_kafka_publisher: Factory = Factory(
        TwichGameKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    # -------------- end change ----------------------

    game_command_repository: Factory = Factory(
        TwichGameMongoRepository,
        db=mongo,
    )

    game_query_repository: Factory = Factory(
        TwichGameElasticRepository,
        db=elastic,
    )

    # ------------- change ---------------------------

    game_kafka_dispatcher: Singleton = Singleton(
        TwichGameKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_GAME_TOPIC,
        repository=game_query_repository,
    )

    # ------------- end change ------------------------

    command_bus: Factory = Factory(
        InMemoryCommandBus,
        command_handlers=Dict(
            {
                ParseTwichGame: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        ParseTwichGameHandler,
                        parser=Factory(
                            TwichGameParser,
                            token=twich_api_token,
                        ),
                        repository=game_command_repository,
                        publisher=game_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichGame: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichGameHandler,
                        repository=game_command_repository,
                        publisher=game_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichGameByName: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichGameByNameHandler,
                        repository=game_command_repository,
                        publisher=game_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    query_bus: Factory = Factory(
        InMemoryQueryBus,
        query_handlers=Dict(
            {
                GetAllTwichGames: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetAllTwichGamesHandler,
                        repository=game_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichGame: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichGameHandler,
                        repository=game_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichGameByName: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichGameByNameHandler,
                        repository=game_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    rest_v1_game_command_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichGameCommandController,
            command_bus=command_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )

    rest_v1_game_query_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichGameQueryController,
            query_bus=query_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )


class TwichStreamContainer(DeclarativeContainer):
    # ---------------- change ------------------------

    twich_api_token: Dependency = Dependency()
    kafka_producer: Dependency = Dependency()
    mongo: Dependency = Dependency()
    elastic: Dependency = Dependency()
    logger: Dependency = Dependency()
    command_exception_handlers: Dependency = Dependency()
    query_exception_handlers: Dependency = Dependency()
    rest_v1_controller_exception_handlers: Dependency = Dependency()

    stream_kafka_publisher: Factory = Factory(
        TwichStreamKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    # -------------- end change ----------------------

    stream_command_repository: Factory = Factory(
        TwichStreamMongoRepository,
        db=mongo,
    )

    stream_query_repository: Factory = Factory(
        TwichStreamElasticRepository,
        db=elastic,
    )

    # ---------------- change ------------------------

    stream_kafka_dispatcher: Singleton = Singleton(
        TwichStreamKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_STREAM_TOPIC,
        repository=stream_query_repository,
    )

    # -------------- end change ----------------------

    command_bus: Factory = Factory(
        InMemoryCommandBus,
        command_handlers=Dict(
            {
                ParseTwichStream: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        ParseTwichStreamHandler,
                        parser=Factory(
                            TwichStreamParser,
                            token=twich_api_token,
                        ),
                        repository=stream_command_repository,
                        publisher=stream_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichStream: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichStreamHandler,
                        repository=stream_command_repository,
                        publisher=stream_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichStreamByUserLogin: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichStreamByUserLoginHandler,
                        repository=stream_command_repository,
                        publisher=stream_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    query_bus: Factory = Factory(
        InMemoryQueryBus,
        query_handlers=Dict(
            {
                GetAllTwichStreams: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetAllTwichStreamsHandler,
                        repository=stream_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichStream: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichStreamHandler,
                        repository=stream_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichStreamByUserLogin: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichStreamByUserLoginHandler,
                        repository=stream_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    rest_v1_stream_command_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichStreamCommandController,
            command_bus=command_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )

    rest_v1_stream_query_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichStreamQueryController,
            query_bus=query_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )


class TwichUserContainer(DeclarativeContainer):
    # ---------------- change ------------------------

    twich_api_token: Dependency = Dependency()
    kafka_producer: Dependency = Dependency()
    mongo: Dependency = Dependency()
    elastic: Dependency = Dependency()
    logger: Dependency = Dependency()
    command_exception_handlers: Dependency = Dependency()
    query_exception_handlers: Dependency = Dependency()
    rest_v1_controller_exception_handlers: Dependency = Dependency()

    user_kafka_publisher: Factory = Factory(
        TwichUserKafkaPublisher,
        kafka_producer=kafka_producer,
    )

    # -------------- end change ----------------------

    user_command_repository: Factory = Factory(
        TwichUserMongoRepository,
        db=mongo,
    )

    user_query_repository: Factory = Factory(
        TwichUserElasticRepository,
        db=elastic,
    )

    # ---------------- change ------------------------

    user_kafka_dispatcher: Singleton = Singleton(
        TwichUserKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=settings.KAFKA_USER_TOPIC,
        repository=user_query_repository,
    )

    # -------------- end change ----------------------

    command_bus: Factory = Factory(
        InMemoryCommandBus,
        command_handlers=Dict(
            {
                ParseTwichUser: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        ParseTwichUserHandler,
                        parser=Factory(
                            TwichUserParser,
                            token=twich_api_token,
                        ),
                        repository=user_command_repository,
                        publisher=user_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichUser: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichUserHandler,
                        repository=user_command_repository,
                        publisher=user_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
                DeleteTwichUserByLogin: Factory(
                    CExceptionHandlingDecorator,
                    command_handler=Factory(
                        DeleteTwichUserByLoginHandler,
                        repository=user_command_repository,
                        publisher=user_kafka_publisher,
                    ),
                    exception_handlers=command_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    query_bus: Factory = Factory(
        InMemoryQueryBus,
        query_handlers=Dict(
            {
                GetAllTwichUsers: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetAllTwichUsersHandler,
                        repository=user_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichUser: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichUserHandler,
                        repository=user_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
                GetTwichUserByLogin: Factory(
                    QExceptionHandlingDecorator,
                    query_handler=Factory(
                        GetTwichUserByLoginHandler,
                        repository=user_query_repository,
                    ),
                    exception_handlers=query_exception_handlers,
                    logger=logger,
                ),
            }
        ),
    )

    rest_v1_user_command_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichUserCommandController,
            command_bus=command_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )

    rest_v1_user_query_controller: Factory = Factory(
        ControllerExceptionHandlingDecorator,
        controller=Factory(
            TwichUserQueryController,
            query_bus=query_bus,
        ),
        exception_handlers=rest_v1_controller_exception_handlers,
    )


class RootContainer(DeclarativeContainer):
    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            'presentation.api.rest.v1.routes.game',
            'presentation.api.rest.v1.routes.stream',
            'presentation.api.rest.v1.routes.user',
        ]
    )

    twich_api_token: Resource = Resource(
        get_twich_api_token,
    )

    kafka_producer: Singleton = Singleton(
        KafkaProducerConnection,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_PRODUCER_API_VERSION,
    )

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

    logger: Singleton = Singleton(
        StreamLogger,
    )

    command_exception_handlers: Dict = Dict(
        {
            ObjectNotFoundException: Singleton(
                ObjectNotFoundExceptionHandler,
                logger=logger,
            ),
            ParserException: Singleton(
                ParserExceptionHandler,
                logger=logger,
            ),
            TwichGetObjectBadRequestException: Singleton(
                TwichGetObjectBadRequestExceptionHandler,
                logger=logger,
            ),
            TwichRequestTimeoutException: Singleton(
                TwichRequestTimeoutExceptionHandler,
                logger=logger,
            ),
            TwichRequestUnauthorizedException: Singleton(
                TwichRequestUnauthorizedExceptionHandler,
                logger=logger,
            ),
            TwichTokenNotObtainedException: Singleton(
                TwichTokenNotObtainedExceptionHandler,
                logger=logger,
            ),
        }
    )

    query_exception_handlers: Dict = Dict(
        {
            ObjectNotFoundException: Singleton(
                ObjectNotFoundExceptionHandler,
                logger=logger,
            ),
        }
    )

    rest_v1_controller_exception_handlers: Dict = Dict(
        {
            ObjectNotFoundException: Singleton(
                RestObjectNotFoundExceptionHandler,
            ),
            ParserException: Singleton(
                RestParserExceptionHandler,
            ),
            TwichGetObjectBadRequestException: Singleton(
                RestTwichGetObjectBadRequestExceptionHandler,
            ),
            TwichRequestTimeoutException: Singleton(
                RestTwichRequestTimeoutExceptionHandler,
            ),
            TwichRequestUnauthorizedException: Singleton(
                RestTwichRequestUnauthorizedExceptionHandler,
            ),
            TwichTokenNotObtainedException: Singleton(
                RestTwichTokenNotObtainedExceptionHandler,
            ),
        }
    )

    game_container: Container = Container(
        TwichGameContainer,
        twich_api_token=twich_api_token,
        kafka_producer=kafka_producer,
        mongo=mongo,
        elastic=elastic,
        logger=logger,
        command_exception_handlers=command_exception_handlers,
        query_exception_handlers=query_exception_handlers,
        rest_v1_controller_exception_handlers=rest_v1_controller_exception_handlers,
    )

    stream_container: Container = Container(
        TwichStreamContainer,
        twich_api_token=twich_api_token,
        kafka_producer=kafka_producer,
        mongo=mongo,
        elastic=elastic,
        logger=logger,
        command_exception_handlers=command_exception_handlers,
        query_exception_handlers=query_exception_handlers,
        rest_v1_controller_exception_handlers=rest_v1_controller_exception_handlers,
    )

    user_container: Container = Container(
        TwichUserContainer,
        twich_api_token=twich_api_token,
        kafka_producer=kafka_producer,
        mongo=mongo,
        elastic=elastic,
        logger=logger,
        command_exception_handlers=command_exception_handlers,
        query_exception_handlers=query_exception_handlers,
        rest_v1_controller_exception_handlers=rest_v1_controller_exception_handlers,
    )
