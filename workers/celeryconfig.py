from kombu import Exchange, Queue

from drfx.config import REDIS_URL


# celery workers
CELERY_BROKER_URL = REDIS_URL

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_QUEUES = (
    Queue('traffic', Exchange('traffic_ex'), routing_key='traffic'),
)
