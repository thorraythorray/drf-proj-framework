from celery import shared_task

# from workers.celery_app import app
from drfx.log import logger
from drfx.constants import CELERY_QUEUE


@shared_task(queue=CELERY_QUEUE.TRAFFIC)
def heartbeat():
    logger.info("bingo.........")
