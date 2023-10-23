from globally.internal import CONF


REDIS_URL = f"redis://:{CONF.REDIS_PASSWD}@{CONF.REDIS_HOST}:{CONF.REDIS_PORT}/{CONF.REDIS_DB}"
