from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILENAME = ".env"
ENV_SEARCH_DEPTH = 3
DEFAULT_DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost:5433/feedbackbrain_db"


def _discover_env_file() -> Path | None:
    start = Path.cwd().resolve()
    candidates = (start, *start.parents)
    for directory in candidates[:ENV_SEARCH_DEPTH]:
        env_file = directory / ENV_FILENAME
        if env_file.is_file():
            return env_file
    return None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_discover_env_file(),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

    APP_NAME: str = "FeedBackBrain"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    DATABASE_URL: str = DEFAULT_DATABASE_URL


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()