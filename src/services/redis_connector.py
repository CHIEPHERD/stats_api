import redis
import os

class RedisConnector:
    class __RedisConnector:
        def __init__(self):
            self.connection = redis.Redis()

    instance = None

    def __new__(self):
        if not RedisConnector.instance:
            RedisConnector.instance = RedisConnector.__RedisConnector()
        return RedisConnector.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self.instance, attr, val)
