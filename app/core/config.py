from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    DATABASE_ECHO: bool = False

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
