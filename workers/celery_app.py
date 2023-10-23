from celery import Celery

from globally.internal.db import REDIS_URL


app = Celery('worker', broker=REDIS_URL)
app.config_from_object('config.celeryconfig')
