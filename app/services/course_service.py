from pymongo.errors import PyMongoError  # type: ignore
from app.database.connection import get_courses_collection
import uuid


def create_course_service(title: str, description: str):
    """
    Service to create a new course in the database.
    """
    courses_collection = get_courses_collection()
    course_id = str(uuid.uuid4())
    new_course = {
        "_id": course_id,
        "title": title,
        "description": description,
    }
    courses_collection.insert_one(new_course)
    return new_course


def get_all_courses_service():
    """
    Service to retrieve all courses from the database.
    """
    courses_collection = get_courses_collection()
    courses = list(courses_collection.find({}))
    for course in courses:
        course["_id"] = str(course["_id"])
    return courses


def get_course_by_id_service(course_id: str):
    """
    Service to retrieve a course by its ID.
    """
    courses_collection = get_courses_collection()
    course = courses_collection.find_one({"_id": course_id})
    if course:
        course["_id"] = str(course["_id"])
    return course


def delete_course_service(course_id: str):
    """
    Service to delete a course by its ID.
    """
    courses_collection = get_courses_collection()
    result = courses_collection.delete_one({"_id": course_id})
    return result.deleted_count