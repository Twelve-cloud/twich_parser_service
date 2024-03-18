"""
settings.py: File, containing settings for a project.
"""


from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings: Class, representing settings for a whole project.

    Bases:
        1) BaseSettings: Base class for all settings classes.
    """

    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: list[str]

    API_NAME: str
    API_VERSION: str
    API_SEM_VERSION: str

    DB_MONGO_NAME: str
    DB_MONGO_USERNAME: str
    DB_MONGO_PASSWORD: str
    DB_MONGO_HOST: str
    DB_MONGO_PORT: int
    DB_MONGO_AUTH_SOURCE: str

    REDIS_PROTOCOL: str
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB_NUMBER: int

    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_PRODUCER_API_VERSION: tuple[int, ...]
    KAFKA_CONSUMER_API_VERSION: tuple[int, ...]
    KAFKA_PARSING_TOPIC: str

    ELASTIC_PROTOCOL: str
    ELASTIC_HOST: str
    ELASTIC_PORT: int

    TWICH_TOKEN_URL: str
    TWICH_CLIENT_ID: str
    TWICH_CLIENT_SECRET: str
    TWICH_API_TOKEN_TYPE: str
    TWICH_API_GRANT_TYPE: str
    TWICH_API_CONTENT_TYPE: str
    TWICH_GET_GAME_BASE_URL: str
    TWICH_GET_USER_BASE_URL: str
    TWICH_GET_STREAM_BASE_URL: str
    KAFKA_GAME_TOPIC: str
    KAFKA_STREAM_TOPIC: str
    KAFKA_USER_TOPIC: str

    class Config:
        case_sensitive: bool = True


settings: Settings = Settings()
