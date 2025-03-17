from fastapi import HTTPException
from app.services.course_service import (
    create_course_service,
    get_all_courses_service,
    get_course_by_id_service,
    delete_course_service,
)
from app.logging_config import get_logger

logger = get_logger()

def create_course_controller(title: str, description: str):
    """
    Controller for creating a course.
    """
    try:
        if not isinstance(title, str) or not isinstance(description, str):
            logger.error("Invalid input data for creating a course")
            raise HTTPException(status_code=400, detail="Invalid input data")
        course = create_course_service(title, description)
        return course
    except Exception as e:
        logger.error(f"Error creating course: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def get_all_courses_controller():
    """
    Controller for retrieving all courses.
    """
    try:
        courses = get_all_courses_service()
        return courses
    except Exception as e:
        logger.error(f"Error retrieving all courses: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def get_course_by_id_controller(course_id: str):
    """
    Controller for retrieving a course by its ID.
    """
    try:
        course = get_course_by_id_service(course_id)
        if not course:
            raise HTTPException(status_code=404, detail=f"The course with ID {course_id} was not found.")
        return course
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

def delete_course_controller(course_id: str):
    """
    Controller for deleting a course by its ID.
    """
    try:
        deleted_count = delete_course_service(course_id)
        if deleted_count == 0:
            raise HTTPException(status_code=404, detail=f"The course with ID {course_id} was not found.")
    except Exception as e:
        logger.error(f"Error deleting course with ID {course_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")