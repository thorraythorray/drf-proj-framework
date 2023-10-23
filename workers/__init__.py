from celery import Celery

from globally.internal.db import REDIS_URL


app = Celery('worker', broker=REDIS_URL)

# Automatic routing
app.conf.task_queues = {
    'traffic': {
        'exchange': 'traffic_ex',
    },
}

app.conf.task_routes = {
    'workers.traffic.*': {
        'queue': 'traffic',
        'routing_key': 'traffic',
    },
}
