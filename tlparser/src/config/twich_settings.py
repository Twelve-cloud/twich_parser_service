"""
twich_settings.py: File, containing settings for a twich app.
"""


from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class TwichSettings(BaseSettings):
    """
    TwichSettings: Settings for a Twich parser.

    Args:
        BaseSettings (_type_): Superclass for a Settings class.
    """

    TWICH_TOKEN_URL: str = 'https://id.twitch.tv/oauth2/token'
    TWICH_CLIENT_ID: str = 'unjl1oyoyg5padmgc5n2em4os2g3mc'
    TWICH_CLIENT_SECRET: str = '5lkjx5z54tydw0nbwda7vgkk5pav5x'
    TWICH_GET_GAME_BASE_URL: str = 'https://api.twitch.tv/helix/games'
    TWICH_GET_USER_BASE_URL: str = 'https://api.twitch.tv/helix/users'
    TWICH_GET_STREAM_BASE_URL: str = 'https://api.twitch.tv/helix/streams'

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: TwichSettings = TwichSettings()
