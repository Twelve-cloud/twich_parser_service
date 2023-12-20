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

    PROJECT_NAME: str = os.environ['PROJECT_NAME']
    API_NAME: str = os.environ['API_NAME']
    API_VERSION: str = os.environ['API_VERSION']
    API_SEM_VERSION: str = os.environ['API_SEM_VERSION']
    BACKEND_CORS_ORIGINS: list[str] = cast(list[str], os.environ['BACKEND_CORS_ORIGINS'])
    DB_MONGO_NAME: str = os.environ['DB_MONGO_NAME']
    DB_MONGO_USERNAME: str = os.environ['DB_MONGO_USERNAME']
    DB_MONGO_PASSWORD: str = os.environ['DB_MONGO_PASSWORD']
    DB_MONGO_HOST: str = os.environ['DB_MONGO_HOST']
    DB_MONGO_PORT: int = cast(int, os.environ['DB_MONGO_PORT'])
    DB_MONGO_AUTH_SOURCE: str = os.environ['DB_MONGO_AUTH_SOURCE']

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: Settings = Settings()
