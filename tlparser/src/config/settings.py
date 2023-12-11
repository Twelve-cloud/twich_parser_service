"""
settings.py: File, containing settings for a entire project.
"""


from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings: Settings for a TwichLamoda project.

    Args:
        BaseSettings (_type_): Superclass for a Settings class.
    """

    PROJECT_NAME: str = 'TwichLamodaParser'
    API_NAME: str = 'api'
    API_VERSION: str = 'v1'
    API_SEM_VERSION: str = '0.0.1'
    BACKEND_CORS_ORIGINS: list[str] = ['*']

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: Settings = Settings()
