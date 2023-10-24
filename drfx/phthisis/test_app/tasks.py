from workers.celery_app import app
from drfx.log import logger


@app.task
def heartbeat():
    logger.info("bingo.........")
