from drfx.log import logger
from workers.celery_app import celery_app


@celery_app.task
def heartbeat(user_id, groups):
    logger.info(f"bingo.........{user_id}, {groups}")
