from fastapi import APIRouter
from typing import Dict, Any
import uuid
import json
import os
from dotenv import load_dotenv

from app.utils import ensure_data_file_exists, load_courses, save_courses
from .models import CourseResponse, CourseCreate
from fastapi import HTTPException

# This is to to modularize our route definitions, improving code organization and maintainability.
# This approach allows us to separate route logic into different files, making the codebase cleaner and easier to manage.
router = APIRouter()

load_dotenv()
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DATA_FILE = os.getenv("DATA_FILE", "/app/data/courses.json")

ensure_data_file_exists()


@router.post("/courses", status_code=201, response_model=CourseResponse)
def create_course(course: CourseCreate):
    """
    Create a new course with the given title and description.
    """
    try:
        if not isinstance(course.title, str) or not isinstance(course.description, str):
            raise HTTPException(status_code=400, detail="Invalid input data")

        courses = load_courses()

        course_id = str(uuid.uuid4())
        new_course = {
            "id": course_id,
            "title": course.title,
            "description": course.description,
        }
        courses[course_id] = new_course

        save_courses(courses)

        return {"data": new_course}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/courses", response_model=Dict[str, Any])
def get_courses():
    """
    Retrieve a list of all courses.
    """
    try:
        courses = load_courses()
        return {"data": list(courses.values())}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/courses/{id}", status_code=200, response_model=CourseResponse)
def get_course(id: str):
    """
    Retrieve a specific course by its ID.
    """
    try:
        courses = load_courses()

        course = courses.get(id)
        if not course:
            raise HTTPException(
                status_code=404, detail=f"The course with ID {id} was not found."
            )

        return {"data": course}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.delete("/courses/{id}", status_code=204)
def delete_course(id: str):
    """
    Delete a specific course by its ID.
    """
    try:
        courses = load_courses()

        course = courses.pop(id, None)
        if not course:
            raise HTTPException(
                status_code=404, detail=f"The course with ID {id} was not found."
            )

        save_courses(courses)

        return {"message": "Course deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
