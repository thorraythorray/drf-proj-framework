from enum import Enum, unique
import os

from django.conf import settings

# Django
DJANGO_SETTING = 'drfx.phthisis.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTING)

ROOT = settings.BASE_DIR
STATIC_ROOT = os.path.join(ROOT, "static")
CONF_DIR = os.path.join(ROOT, 'config')
ENV = os.environ.get('DRF_ENV', 'local')

# DB
REDIS_URL = f"redis://:{settings.REDIS_PASSWD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"

# celery queues
@unique
class CeleryQueue(Enum):
    TRAFFIC = 'traffic'
