from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.config.telegram import TelegramConfig


class Config(BaseSettings):
    debug: bool = False

    telegram: TelegramConfig = None

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file='.env',
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )


config: Config = Config()
