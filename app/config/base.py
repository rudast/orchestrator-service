from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.config.database import PostgresConfig
from app.config.telegram import TelegramConfig

BASE_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    debug: bool = False
    telegram: TelegramConfig
    postgres: PostgresConfig

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=BASE_DIR / '.env',
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )


@lru_cache(maxsize=1)
def get_config() -> Config:
    return Config()
