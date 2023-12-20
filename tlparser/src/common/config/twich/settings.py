"""
settings.py: File, containing settings for a twich app.
"""


import os
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class TwichSettings(BaseSettings):
    """
    TwichSettings: Settings for a Twich parser.

    Args:
        BaseSettings (_type_): Superclass for a Settings class.
    """

    TWICH_TOKEN_URL: str = os.environ['TWICH_TOKEN_URL']
    TWICH_CLIENT_ID: str = os.environ['TWICH_CLIENT_ID']
    TWICH_CLIENT_SECRET: str = os.environ['TWICH_CLIENT_SECRET']
    TWICH_GET_GAME_BASE_URL: str = os.environ['TWICH_GET_GAME_BASE_URL']
    TWICH_GET_USER_BASE_URL: str = os.environ['TWICH_GET_USER_BASE_URL']
    TWICH_GET_STREAM_BASE_URL: str = os.environ['TWICH_GET_STREAM_BASE_URL']

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: TwichSettings = TwichSettings()
