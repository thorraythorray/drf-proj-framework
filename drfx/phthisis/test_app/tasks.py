from celery import shared_task

# from workers.celery_app import app
from drfx.log import logger
from drfx.config import CeleryQueue
from workers.celery_app import celery_app


@celery_app.task
def heartbeat():
    logger.info("bingo.........")
