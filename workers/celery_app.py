from celery import Celery

from drfx.config import settings


app = Celery('drfx_workers')
# app.config_from_object('celeryconfig', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)
