import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfx.settings.dev')

app = Celery('drf_workers')
app.config_from_object('celeryconfig')
app.autodiscover_tasks(['celery_tasks.sms', ])
