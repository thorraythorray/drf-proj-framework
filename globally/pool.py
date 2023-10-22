from multiprocessing import cpu_count

import pymysql
from dbutils.pooled_db import PooledDB
from redis import Redis

from globally.config import setting_dict
from utils.singleton import singleton


@singleton
class RedisDBClient:
    def __init__(self, params):
        self.host = params["REDIS_HOST"]
        self.port = params["REDIS_PORT"]
        self.password = params["REDIS_PASSWD"]
        self.redis_db = params.get("REDIS_DB", 8)
        self.redis = Redis.from_url(f"redis://:{self.password}@{self.host}:{self.port}/{self.redis_db}")


redis_pool = RedisDBClient(setting_dict()).redis


@singleton
class DBClient:
    def __init__(self, params):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=(cpu_count() * 2) + 1,
            blocking=True,  # 阻塞等待
            setsession=[],
            ping=0,
            host=params["MYSQL_HOST"],
            port=params["MYSQL_PORT"],
            user=params["MYSQL_USER"],
            password=params["MYSQL_PASSWD"],
            database=params["MYSQL_DB"],
            charset='utf8'
        )


db_pool = DBClient(setting_dict()).pool
