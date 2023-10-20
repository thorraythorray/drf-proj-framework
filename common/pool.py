from multiprocessing import cpu_count

import pymysql
from dbutils.pooled_db import PooledDB
from redis import Redis

from etc import CONF
from utils.singleton import singleton


@singleton
class RedisDBClient:
    def __init__(self, params):
        self.host = params["REDIS_HOST"]
        self.port = params["REDIS_PORT"]
        self.db = params["REDIS_DB"]
        self.password = params["REDIS_PWD"]
        self.redis_db = params.get("REDIS_DB", 8)
        self.redis = Redis.from_url(f"redis://:{self.password}@{self.host}:{self.port}/{self.redis_db}")


redis_pool = RedisDBClient(CONF).redis


@singleton
class DBClient:
    def __init__(self, params):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=(cpu_count() * 2) + 1,
            blocking=True,  # 阻塞等待
            setsession=[],
            ping=0,
            host=params["DB_HOST"],
            port=params["DB_PORT"],
            user=params["DB_USER"],
            password=params["DB_PASS"],
            database=params["DB_NAME"],
            charset='utf8'
        )


db_pool = DBClient(CONF).pool
