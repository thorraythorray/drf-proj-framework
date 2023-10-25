from celery import Celery

from drfx.config import settings


celery_app = Celery('drfx_workers')
celery_app.config_from_object('workers.celeryconfig', namespace='CELERY')
# app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(settings.INSTALLED_APPS)
