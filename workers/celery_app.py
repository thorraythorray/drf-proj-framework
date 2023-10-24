import os

from celery import Celery
from django.conf import settings

from drfx.config import DJANGO_SETTING


os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTING)

app = Celery('drfx_workers')
# app.config_from_object('celeryconfig')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)
