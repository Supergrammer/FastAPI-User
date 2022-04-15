from pydantic import BaseSettings
from functools import lru_cache

import os


class Settings(BaseSettings):
    app_name: str = "FastAPI User Back-end"
    mode: str

# Database Settings (.env)
# NOTE: Need Factory Method??
class DatabaseSettings(BaseSettings):
    database: str
    database_user: str
    database_password: str
    database_server: str
    database_name: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings(_env_file=f".env.{os.getenv('MODE')}")


@lru_cache
def get_database_settings():
    return DatabaseSettings(_env_file=f".env.{os.getenv('MODE')}")
