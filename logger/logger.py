import logging.config

from config.log_config import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("app")
print("initialized", logger)