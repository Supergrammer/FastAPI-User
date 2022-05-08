from typing import AsyncIterator

from aioredis import from_url, Redis


def init_redis_pool(host: str, password: str) -> AsyncIterator[Redis]:
    redis_pool = from_url(url=f"redis://{host}", password=password, encoding="utf-8", decode_responses=True)

    print(redis_pool)
    return redis_pool