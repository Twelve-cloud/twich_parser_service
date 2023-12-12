"""
lamoda_settings.py: File, containing settings for a lamoda app.
"""


from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class LamodaSettings(BaseSettings):
    """
    LamodaSettings: Settings for a Lamoda parser.

    Args:
        BaseSettings (_type_): Superclass for a Settings class.
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(case_sensitive=True)


settings: LamodaSettings = LamodaSettings()
