from celery import shared_task

# from workers.celery_app import app
from drfx.log import logger
from drfx.config import CeleryQueue


@shared_task(queue=CeleryQueue.TRAFFIC)
def heartbeat():
    logger.info("bingo.........")
