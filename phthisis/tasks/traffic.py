from globally.log import logger
from workers.celery_app import app


@app.task
def heartbeat():
    logger.info("bingo.........")
