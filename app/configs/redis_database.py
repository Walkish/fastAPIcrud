import os
from redis import asyncio as aioredis

REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

redis = aioredis.from_url(
    f"redis://localhost",
    password=REDIS_PASSWORD,
    encoding="utf8",
    decode_responses=True,
)
