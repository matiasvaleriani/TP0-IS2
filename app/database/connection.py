import os
from dotenv import load_dotenv
from pymongo import MongoClient  # type: ignore

load_dotenv()

# Detect if we are in test mode
IS_TESTING = os.getenv("PYTEST_CURRENT_TEST") is not None

MONGODB_URI = os.getenv("TEST_MONGODB_URI") if IS_TESTING else os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("TEST_MONGODB_DB_NAME") if IS_TESTING else os.getenv("MONGODB_DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]


def get_courses_collection():
    """
    Get the MongoDB collection for courses.

    Returns:
        - Collection: The MongoDB collection object for courses.
    """
    return db.courses