import redis

from tools.config import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_PASSWORD,
)

CHARSET = "utf-8"

class RedisConn:
    def __init__(self):
        self.r = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            charset=CHARSET
        )
        self.id = 0

    def add(self, data):
        pass

    def del(self, data):
        pass

    def get_id(self, data):
        pass
