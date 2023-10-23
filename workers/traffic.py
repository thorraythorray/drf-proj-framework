from globally.log import logger
from workers import app


@app.task
def heartbeat():
    logger.info("bingo.........")
