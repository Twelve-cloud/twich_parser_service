"""
settings.py: File, containing settings for a entire project.
"""


import os
from typing import ClassVar, cast
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings: Settings for a TwichLamoda project.

    Args:
        BaseSettings (_type_): Superclass for a Settings class.
    """

    KAFKA_BOOTSTRAP_SERVERS: str = os.environ['KAFKA_BOOTSTRAP_SERVERS']
    KAFKA_CONSUMER_API_VERSION: tuple[int, ...] = cast(
        tuple[int, ...],
        os.environ['KAFKA_CONSUMER_API_VERSION'],
    )
    KAFKA_PARSING_TOPIC: str = os.environ['KAFKA_PARSING_TOPIC']
    TLPARSER_LAMODA_PRODUCTS_PARSE_URL: str = os.environ['TLPARSER_LAMODA_PRODUCTS_PARSE_URL']
    TLPARSER_TWICH_GAME_PARSE_URL: str = os.environ['TLPARSER_TWICH_GAME_PARSE_URL']
    TLPARSER_TWICH_STREAM_PARSE_URL: str = os.environ['TLPARSER_TWICH_STREAM_PARSE_URL']
    TLPARSER_TWICH_USER_PARSE_URL: str = os.environ['TLPARSER_TWICH_USER_PARSE_URL']

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: Settings = Settings()
