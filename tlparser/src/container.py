"""
container.py: File, containing container that describe all dependencies in the project.
"""


from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton
from application.services.lamoda.kafka.products_service import LamodaProductsKafkaService
from application.services.lamoda.rest.products_service import LamodaProductsRestService
from application.services.twich.kafka.game_service import TwichGameKafkaService
from application.services.twich.kafka.stream_service import TwichStreamKafkaService
from application.services.twich.kafka.user_service import TwichUserKafkaService
from application.services.twich.rest.game_service import TwichGameRestService
from application.services.twich.rest.stream_service import TwichStreamRestService
from application.services.twich.rest.user_service import TwichUserRestService
from common.config.base.settings import settings
from common.config.lamoda.settings import settings as lamoda_settings
from common.config.twich.settings import settings as twich_settings
from domain.dependencies.twich.token_dependency import TwichAPIToken
from domain.services.lamoda.products_service import LamodaProductsDomainService
from domain.services.twich.game_service import TwichGameDomainService
from domain.services.twich.stream_service import TwichStreamDomainService
from domain.services.twich.user_service import TwichUserDomainService
from infrastructure.connections.elastic.database import ElasticSearchDatabase
from infrastructure.connections.kafka.producer import KafkaProducerConnection
from infrastructure.connections.mongo.database import MongoDatabase
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
from presentation.dispatchers.lamoda.kafka.products_dispatcher import LamodaProductsKafkaDispatcher
from presentation.dispatchers.twich.kafka.game_dispatcher import TwichGameKafkaDispatcher
from presentation.dispatchers.twich.kafka.stream_dispatcher import TwichStreamKafkaDispatcher
from presentation.dispatchers.twich.kafka.user_dispatcher import TwichUserKafkaDispatcher


class Container(DeclarativeContainer):
    """
    Container: Class, that describe all dependencies in the project.

    Args:
        DeclarativeContainer (_type_): Base superclass for a Container class.
    """

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            'presentation.api.rest.v1.endpoints.lamoda.products',
            'presentation.api.rest.v1.endpoints.twich.game',
            'presentation.api.rest.v1.endpoints.twich.user',
            'presentation.api.rest.v1.endpoints.twich.stream',
        ],
    )

    # ------------------------------------- Dependencies ------------------------------------------

    twich_api_token: Singleton = Singleton(
        TwichAPIToken,
    )

    # ------------------------------------- Domain Services ---------------------------------------

    lamoda_products_domain_service: Factory = Factory(
        LamodaProductsDomainService,
    )

    twich_game_domain_service: Factory = Factory(
        TwichGameDomainService,
        token=twich_api_token,
    )

    twich_user_domain_service: Factory = Factory(
        TwichUserDomainService,
        token=twich_api_token,
    )

    twich_stream_domain_service: Factory = Factory(
        TwichStreamDomainService,
        token=twich_api_token,
    )

    # ------------------------------------- Kafka -------------------------------------------------

    kafka_producer: Singleton = Singleton(
        KafkaProducerConnection,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_PRODUCER_API_VERSION,
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

    # ----------------------------------- Services -------------------------------------------------

    lamoda_products_rest_w_service: Factory = Factory(
        LamodaProductsRestService,
        domain_service=lamoda_products_domain_service,
        repository=lamoda_products_mongo_repository,
        publisher=lamoda_products_kafka_publisher,
    )

    lamoda_products_rest_r_service: Factory = Factory(
        LamodaProductsRestService,
        domain_service=lamoda_products_domain_service,
        repository=lamoda_products_elastic_repository,
        publisher=lamoda_products_kafka_publisher,
    )

    twich_game_rest_w_service: Factory = Factory(
        TwichGameRestService,
        domain_service=twich_game_domain_service,
        repository=twich_game_mongo_repository,
        publisher=twich_game_kafka_publisher,
    )

    twich_game_rest_r_service: Factory = Factory(
        TwichGameRestService,
        domain_service=twich_game_domain_service,
        repository=twich_game_elastic_repository,
        publisher=twich_game_kafka_publisher,
    )

    twich_user_rest_w_service: Factory = Factory(
        TwichUserRestService,
        domain_service=twich_user_domain_service,
        repository=twich_user_mongo_repository,
        publisher=twich_user_kafka_publisher,
    )

    twich_user_rest_r_service: Factory = Factory(
        TwichUserRestService,
        domain_service=twich_user_domain_service,
        repository=twich_user_elastic_repository,
        publisher=twich_user_kafka_publisher,
    )

    twich_stream_rest_w_service: Factory = Factory(
        TwichStreamRestService,
        domain_service=twich_stream_domain_service,
        repository=twich_stream_mongo_repository,
        publisher=twich_stream_kafka_publisher,
    )

    twich_stream_rest_r_service: Factory = Factory(
        TwichStreamRestService,
        domain_service=twich_stream_domain_service,
        repository=twich_stream_elastic_repository,
        publisher=twich_stream_kafka_publisher,
    )

    lamoda_products_kafka_service: Factory = Factory(
        LamodaProductsKafkaService,
        domain_service=lamoda_products_domain_service,
        repository=lamoda_products_elastic_repository,
        publisher=lamoda_products_kafka_publisher,
    )

    twich_game_kafka_service: Factory = Factory(
        TwichGameKafkaService,
        domain_service=twich_game_domain_service,
        repository=twich_game_elastic_repository,
        publisher=twich_game_kafka_publisher,
    )

    twich_user_kafka_service: Factory = Factory(
        TwichUserKafkaService,
        domain_service=twich_user_domain_service,
        repository=twich_user_elastic_repository,
        publisher=twich_user_kafka_publisher,
    )

    twich_stream_kafka_service: Factory = Factory(
        TwichStreamKafkaService,
        domain_service=twich_stream_domain_service,
        repository=twich_stream_elastic_repository,
        publisher=twich_stream_kafka_publisher,
    )

    # --------------------------------- Dispatchers ------------------------------------------------

    lamoda_products_kafka_dispatcher: Singleton = Singleton(
        LamodaProductsKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=lamoda_settings.KAFKA_PRODUCT_TOPIC,
        service=lamoda_products_kafka_service,
    )

    twich_game_kafka_dispatcher: Singleton = Singleton(
        TwichGameKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_GAME_TOPIC,
        service=twich_game_kafka_service,
    )

    twich_user_kafka_dispatcher: Singleton = Singleton(
        TwichUserKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_USER_TOPIC,
        service=twich_user_kafka_service,
    )

    twich_stream_kafka_dispatcher: Singleton = Singleton(
        TwichStreamKafkaDispatcher,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        api_version=settings.KAFKA_CONSUMER_API_VERSION,
        topic=twich_settings.KAFKA_STREAM_TOPIC,
        service=twich_stream_kafka_service,
    )

    # ---------------------------------- Controllers -----------------------------------------------

    lamoda_products_w_controller: Factory = Factory(
        LamodaProductsController,
        service=lamoda_products_rest_w_service,
    )

    lamoda_products_r_controller: Factory = Factory(
        LamodaProductsController,
        service=lamoda_products_rest_r_service,
    )

    twich_game_w_controller: Factory = Factory(
        TwichGameController,
        service=twich_game_rest_w_service,
    )

    twich_game_r_controller: Factory = Factory(
        TwichGameController,
        service=twich_game_rest_r_service,
    )

    twich_user_w_controller: Factory = Factory(
        TwichUserController,
        service=twich_user_rest_w_service,
    )

    twich_user_r_controller: Factory = Factory(
        TwichUserController,
        service=twich_user_rest_r_service,
    )

    twich_stream_w_controller: Factory = Factory(
        TwichStreamController,
        service=twich_stream_rest_w_service,
    )

    twich_stream_r_controller: Factory = Factory(
        TwichStreamController,
        service=twich_stream_rest_r_service,
    )
