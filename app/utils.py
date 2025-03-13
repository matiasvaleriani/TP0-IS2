import json
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]


def get_courses_collection():
    return db.courses


def create_rfc7807_error_response(
    status_code: int, title: str, detail: str, instance: str
):
    return JSONResponse(
        status_code=status_code,
        content={
            "type": "about:blank",
            "title": title,
            "status": status_code,
            "detail": detail,
            "instance": instance,
        },
    )
