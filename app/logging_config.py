from loguru import logger  # type: ignore
import sys
import os

environment = os.getenv("ENVIRONMENT", "production")
IS_TESTING = os.getenv("PYTEST_CURRENT_TEST") is not None

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger.remove()

# Do not write logs if we are in test mode
if not IS_TESTING:
    logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
    if environment == "development":
        logger.add(
            f"{log_directory}/app.log",
            rotation="1 MB",
            retention="10 days",
            level="DEBUG",
        )

    logger.info(f"Application is running in '{environment}' environment.")


def get_logger():
    return logger
