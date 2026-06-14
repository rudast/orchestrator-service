from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.config.telegram import TelegramConfig


class Config(BaseSettings):
    debug: bool = False
    telegram: TelegramConfig

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file='.env',
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )


@lru_cache(maxsize=1)
def get_config() -> Config:
    return Config()
