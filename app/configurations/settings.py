from pydantic import BaseSettings
from functools import lru_cache

import os

env_file = f".env.{os.getenv('MODE')}"


class AppSettings(BaseSettings):
    # App Settings(.env)
    # NOTE: Need Factory Method??
    app_name: str = "FastAPI User Back-end"
    mode: str


class UserDatabaseSettings(BaseSettings):
    # User Database Settings (.env)
    database: str
    database_user: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str

    class Config:
        env_file = ".env"


class RedisSettings(BaseSettings):
    # Redis Settings (.env)
    redis_password: str
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"


class AuthModuleSettings(BaseSettings):
    # Auth Module Settings (.env)
    secret_key: str
    algorithm: str

    access_token_expiration_period: int
    refresh_token_expiration_period: int

    password_expiration_period: int
    previous_password_history_match_count: int

    class Config:
        env_file = ".env"


@lru_cache
def get_app_settings():
    return AppSettings(_env_file=env_file)


@lru_cache
def get_user_database_settings():
    return UserDatabaseSettings(_env_file=env_file)


@lru_cache
def get_redis_settings():
    return RedisSettings(_env_file=env_file)


@lru_cache
def get_auth_module_settings():
    return AuthModuleSettings(_env_file=env_file)
