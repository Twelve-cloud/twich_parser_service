"""
container.py: File, containing container that describe all dependencies in the project.
"""


from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton
from application.dependencies.twich.token_dependency import TwichAPIToken
from application.services.lamoda.products_service import LamodaProductsService
from application.services.twich.game_service import TwichGameService
from application.services.twich.stream_service import TwichStreamService
from application.services.twich.user_service import TwichUserService
from common.config.base.settings import settings
from common.config.lamoda.settings import settings as lamoda_settings
from common.config.twich.settings import settings as twich_settings
from infrastructure.connections.elastic.database import ElasticSearchDatabase
from infrastructure.connections.kafka.producer import KafkaProducerConnection
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.dispatchers.lamoda.kafka.products_dispatcher import (
    LamodaProductsKafkaDispatcher,
)
from infrastructure.dispatchers.twich.kafka.game_dispatcher import TwichGameKafkaDispatcher
from infrastructure.dispatchers.twich.kafka.stream_dispatcher import TwichStreamKafkaDispatcher
from infrastructure.dispatchers.twich.kafka.user_dispatcher import TwichUserKafkaDispatcher
from infrastructure.publishers.lamoda.kafka.products_publisher import LamodaProductsKafkaPublisher
from infrastructure.publishers.twich.kafka.game_publisher import TwichGameKafkaPublisher
from infrastructure.publishers.twich.kafka.stream_publisher import TwichStreamKafkaPublisher
from infrastructure.publishers.twich.kafka.user_publisher import TwichUserKafkaPublisher
from infrastructure.repositories.lamoda.elastic.products_repository import (
    LamodaProductsElasticRepository,
)
from infrastructure.repositories.lamoda.mongo.products_repository import (
    LamodaProductsMongoRepository,
)
from infrastructure.repositories.twich.elastic.game_repository import TwichGameElasticRepository
from infrastructure.repositories.twich.elastic.stream_repository import TwichStreamElasticRepository
from infrastructure.repositories.twich.elastic.user_repository import TwichUserElasticRepository
from infrastructure.repositories.twich.mongo.game_repository import TwichGameMongoRepository
from infrastructure.repositories.twich.mongo.stream_repository import TwichStreamMongoRepository
from infrastructure.repositories.twich.mongo.user_repository import TwichUserMongoRepository
from presentation.controllers.lamoda.products_controller import LamodaProductsController
from presentation.controllers.twich.game_controller import TwichGameController
from presentation.controllers.twich.stream_controller import TwichStreamController
from presentation.controllers.twich.user_controller import TwichUserController


class Container(DeclarativeContainer):
    """
    Container: Class, that describe all dependencies in the project.

    Args:
        DeclarativeContainer (_type_): Base superclass for a Container class.
    """

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            'presentation.api.v1.endpoints.rest.lamoda.products',
            'presentation.api.v1.endpoints.rest.twich.game',
            'presentation.api.v1.endpoints.rest.twich.user',
            'presentation.api.v1.endpoints.rest.twich.stream',
        ],
    )

    # ------------------------------------- Kafka -------------------------------------------------

    kafka_producer: Singleton = Singleton(
        KafkaProducerConnection,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_PRODUCER_API_VERSION,
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

    # ------------------------------------- Other --------------------------------------------------

    twich_api_token: Singleton = Singleton(
        TwichAPIToken,
    )

    # ---------------------------------- Repositories ----------------------------------------------

    lamoda_products_mongo_repository: Factory = Factory(
        LamodaProductsMongoRepository,
        db=mongo,
    )

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

    lamoda_products_elastic_repository: Factory = Factory(
        LamodaProductsElasticRepository,
        db=elastic,
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

    # ---------------------------------- Publishers ------------------------------------------------

    lamoda_products_kafka_publisher: Factory = Factory(
        LamodaProductsKafkaPublisher,
        kafka_producer=kafka_producer,
    )

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

    # --------------------------------- Dispatchers ------------------------------------------------

    lamoda_products_kafka_dispatcher: Singleton = Singleton(
        LamodaProductsKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=lamoda_settings.KAFKA_PRODUCT_TOPIC,
        repository=lamoda_products_elastic_repository,
    )

    twich_game_kafka_dispatcher: Singleton = Singleton(
        TwichGameKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_GAME_TOPIC,
        repository=twich_game_elastic_repository,
    )

    twich_user_kafka_dispatcher: Singleton = Singleton(
        TwichUserKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_USER_TOPIC,
        repository=twich_user_elastic_repository,
    )

    twich_stream_kafka_dispatcher: Singleton = Singleton(
        TwichStreamKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_STREAM_TOPIC,
        repository=twich_stream_elastic_repository,
    )

    # ----------------------------------- Services -------------------------------------------------

    lamoda_products_w_service: Factory = Factory(
        LamodaProductsService,
        repository=lamoda_products_mongo_repository,
        publisher=lamoda_products_kafka_publisher,
    )

    lamoda_products_r_service: Factory = Factory(
        LamodaProductsService,
        repository=lamoda_products_elastic_repository,
        publisher=lamoda_products_kafka_publisher,
    )

    twich_game_w_service: Factory = Factory(
        TwichGameService,
        repository=twich_game_mongo_repository,
        publisher=twich_game_kafka_publisher,
        token=twich_api_token,
    )

    twich_game_r_service: Factory = Factory(
        TwichGameService,
        repository=twich_game_elastic_repository,
        publisher=twich_game_kafka_publisher,
        token=twich_api_token,
    )

    twich_user_w_service: Factory = Factory(
        TwichUserService,
        repository=twich_user_mongo_repository,
        publisher=twich_user_kafka_publisher,
        token=twich_api_token,
    )

    twich_user_r_service: Factory = Factory(
        TwichUserService,
        repository=twich_user_elastic_repository,
        publisher=twich_user_kafka_publisher,
        token=twich_api_token,
    )

    twich_stream_w_service: Factory = Factory(
        TwichStreamService,
        repository=twich_stream_mongo_repository,
        publisher=twich_stream_kafka_publisher,
        token=twich_api_token,
    )

    twich_stream_r_service: Factory = Factory(
        TwichStreamService,
        repository=twich_stream_elastic_repository,
        publisher=twich_stream_kafka_publisher,
        token=twich_api_token,
    )

    # ---------------------------------- Controllers -----------------------------------------------

    lamoda_products_w_controller: Factory = Factory(
        LamodaProductsController,
        service=lamoda_products_w_service,
    )

    lamoda_products_r_controller: Factory = Factory(
        LamodaProductsController,
        service=lamoda_products_r_service,
    )

    twich_game_w_controller: Factory = Factory(
        TwichGameController,
        service=twich_game_w_service,
    )

    twich_game_r_controller: Factory = Factory(
        TwichGameController,
        service=twich_game_r_service,
    )

    twich_user_w_controller: Factory = Factory(
        TwichUserController,
        service=twich_user_w_service,
    )

    twich_user_r_controller: Factory = Factory(
        TwichUserController,
        service=twich_user_r_service,
    )

    twich_stream_w_controller: Factory = Factory(
        TwichStreamController,
        service=twich_stream_w_service,
    )

    twich_stream_r_controller: Factory = Factory(
        TwichStreamController,
        service=twich_stream_r_service,
    )
