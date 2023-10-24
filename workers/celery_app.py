import os

from celery import Celery

from drfx.config import DjangoSetting


os.environ.setdefault('DJANGO_SETTINGS_MODULE', DjangoSetting)

app = Celery('drfx_workers')
# app.config_from_object('celeryconfig')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
