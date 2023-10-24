from enum import Enum, unique


@unique
class CELERY_QUEUE(Enum):
    TRAFFIC = 'traffic'
