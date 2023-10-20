import os
import logging
import logging.config

import yaml

from etc import ROOT


def init_log():
    logging.logThreads = 0
    logging.logProcesses = 0
    logging._srcfile = None
    log_yaml = os.path.join(ROOT, "config/logging.yaml")
    with open(log_yaml) as log_file:
        logging_config = yaml.safe_load(log_file)
    logging.config.dictConfig(logging_config)
    _logger = logging.getLogger(f'app.prod')
    _logger.name = __name__
    return _logger


logger = init_log()
