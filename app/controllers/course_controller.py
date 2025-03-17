from fastapi import HTTPException
from app.services.course_service import (
    create_course_service,
    get_all_courses_service,
    get_course_by_id_service,
    delete_course_service,
)


def create_course_controller(title: str, description: str):
    """
    Controller for creating a course.
    """
    if not isinstance(title, str) or not isinstance(description, str):
        raise HTTPException(status_code=400, detail="Invalid input data")
    return create_course_service(title, description)


def get_all_courses_controller():
    """
    Controller for retrieving all courses.
    """
    return get_all_courses_service()


def get_course_by_id_controller(course_id: str):
    """
    Controller for retrieving a course by its ID.
    """
    course = get_course_by_id_service(course_id)
    if not course:
        raise HTTPException(status_code=404, detail=f"The course with ID {course_id} was not found.")
    return course


def delete_course_controller(course_id: str):
    """
    Controller for deleting a course by its ID.
    """
    deleted_count = delete_course_service(course_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"The course with ID {course_id} was not found.")