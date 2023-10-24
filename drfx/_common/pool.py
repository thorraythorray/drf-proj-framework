from multiprocessing import cpu_count

import pymysql
from dbutils.pooled_db import PooledDB
from redis import Redis

from helper.singleton import singleton
from drfx import config


@singleton
class RedisDBClient:
    def __init__(self, url):
        self.redis = Redis.from_url(url)


redis_pool = RedisDBClient(config.REDIS_URL).redis


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


db_pool = DBClient().pool
