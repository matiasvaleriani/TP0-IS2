from loguru import logger  # type: ignore
import sys
import os

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger.remove()
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add(
    f"{log_directory}/app.log", rotation="1 MB", retention="10 days", level="DEBUG"
)


def get_logger():
    return logger
