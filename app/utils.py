import json
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()
DATA_FILE = os.getenv("DATA_FILE", "/app/data/courses.json")

def load_courses():
    """
    Loads courses from the JSON data file.
    """
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_courses(courses):
    """
    Saves courses to the JSON data file.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(courses, f)

def ensure_data_file_exists():
    """
    Ensures the data file exists, creating it if necessary.
    """
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)

def create_rfc7807_error_response(status_code: int, title: str, detail: str, instance: str):
    return JSONResponse(
        status_code=status_code,
        content={
            
            "type": "about:blank",
            "title": title,
            "status": status_code,
            "detail": detail,
            "instance": instance
        }
    )