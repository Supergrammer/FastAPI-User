from sqlalchemy.orm import Session
from aioredis import Redis

from app.modules import auth_module
from app.modules.auth_module import REFRESH_TOKEN_EXPIRATION_PERIOD

from app.schemas import user_schema

from .common import get_user_by_email

from app.http_exception import refresh_token_invalid_exception


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    db_user = get_user_by_email(db=db, email=email)

    if not db_user or \
            not auth_module.verify_password(password, db_user.password.hashed_password):
        return False

    return db_user


async def get_authentication(
    redis: Redis,
    user: user_schema.User
):
    auth = auth_module.get_token(email=user.email)
    await redis.set(str(user.id), auth.get("refresh_token"), ex=REFRESH_TOKEN_EXPIRATION_PERIOD)

    return auth


async def refresh_authentication(
    redis: Redis,
    user: user_schema.User,
    refresh_token: str
):
    stored_token = await redis.get(str(user.id))

    if not stored_token or \
            not refresh_token == stored_token:
        raise refresh_token_invalid_exception

    return await get_authentication(redis=redis, user=user)


async def expire_authentication(
    redis: Redis,
    user: user_schema.User,
):
    await redis.delete(str(user.id))
