from aioredis import Redis, from_url
from typing import AsyncIterator

from .settings import get_redis_settings

rds = get_redis_settings()


async def get_redis_pool() -> AsyncIterator[Redis]:
    redis_pool = await from_url(url=f"redis://{rds.redis_host}:{rds.redis_port}",
                                password=rds.redis_password, db=0, encoding="utf-8", decode_responses=True)
    try:
        yield redis_pool
    finally:
        await redis_pool.close()
