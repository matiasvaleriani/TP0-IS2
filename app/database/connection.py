import os
from dotenv import load_dotenv
from pymongo import MongoClient # type: ignore

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]


def get_courses_collection():
    """
    Get the MongoDB collection for courses.

    Returns:
        - Collection: The MongoDB collection object for courses.
    """
    return db.courses
