from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import os
from dotenv import load_dotenv
from loguru import logger  # type: ignore
from pymongo.errors import PyMongoError  # type: ignore
import uuid
from app.utils import get_courses_collection
from app.models import CourseResponse, CourseCreate

router = APIRouter()

load_dotenv()
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@router.post("/courses", status_code=201, response_model=CourseResponse)
def create_course(course: CourseCreate):
    """
    Create a new course.

    Parameters:
        - course (CourseCreate): Contains title (str) and description (str).

    Returns:
        - 201 Created: The created course with its ID.
        - 400 Bad Request: If input data is invalid.
        - 500 Internal Server Error: If a database error occurs.
    """
    try:
        if not isinstance(course.title, str) or not isinstance(course.description, str):
            logger.error("Invalid input data: {}", course)
            raise HTTPException(status_code=400, detail="Invalid input data")

        courses_collection = get_courses_collection()

        course_id = str(uuid.uuid4())
        new_course = {
            "_id": course_id,
            "title": course.title,
            "description": course.description,
        }
        courses_collection.insert_one(new_course)

        logger.info("Course created successfully with ID: {}", course_id)
        return {"data": new_course}
    except PyMongoError as e:
        logger.exception("An error occurred while interacting with the database.")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while interacting with the database.",
        )
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/courses", response_model=Dict[str, Any])
def get_courses():
    """
    Retrieve all courses.

    Returns:
        - 200 OK: A list of all courses.
        - 500 Internal Server Error: If a database error occurs.
    """
    try:
        logger.info("Retrieving all courses")
        courses_collection = get_courses_collection()
        courses = list(courses_collection.find({}))
        for course in courses:
            course["_id"] = str(course["_id"])
        return {"data": courses}
    except PyMongoError as e:
        logger.exception("An error occurred while interacting with the database.")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while interacting with the database.",
        )
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/courses/{id}", status_code=200, response_model=CourseResponse)
def get_course(id: str):
    """
    Retrieve a specific course by its ID.

    Parameters:
        - id (str): The unique identifier of the course.

    Returns:
        - 200 OK: The requested course.
        - 404 Not Found: If the course does not exist.
        - 500 Internal Server Error: If a database error occurs.
    """

    try:
        logger.info("Retrieving course with ID: {}", id)
        courses_collection = get_courses_collection()
        course = courses_collection.find_one({"_id": id})
        if not course:
            raise HTTPException(
                status_code=404, detail=f"The course with ID {id} was not found."
            )
        course["_id"] = str(course["_id"])
        return {"data": course}
    except PyMongoError as e:
        logger.exception("An error occurred while interacting with the database.")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while interacting with the database.",
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.delete("/courses/{id}", status_code=204)
def delete_course(id: str):
    """
    Delete a specific course by its ID.

    Parameters:
        - id (str): The unique identifier of the course.

    Returns:
        - 204 No Content: If the course was deleted successfully.
        - 404 Not Found: If the course does not exist.
        - 500 Internal Server Error: If a database error occurs.
    """
    try:
        courses_collection = get_courses_collection()
        result = courses_collection.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404, detail=f"The course with ID {id} was not found."
            )
        logger.info("Course with ID {} deleted successfully", id)
        return {"message": "Course deleted successfully"}
    except PyMongoError as e:
        logger.exception("An error occurred while interacting with the database.")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while interacting with the database.",
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
