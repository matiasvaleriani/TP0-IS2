from pymongo.errors import PyMongoError  # type: ignore
from app.database.connection import get_courses_collection
from app.logging_config import get_logger
import uuid

logger = get_logger()


def create_course_service(title: str, description: str):
    """
    Service to create a new course in the database.
    """
    try:
        courses_collection = get_courses_collection()
        course_id = str(uuid.uuid4())
        new_course = {
            "_id": course_id,
            "title": title,
            "description": description,
        }
        courses_collection.insert_one(new_course)
        logger.info(f"Course created in database: {course_id}")
        return new_course
    except PyMongoError as e:
        logger.error(f"Database error while creating course: {e}")
        raise


def get_all_courses_service():
    """
    Service to retrieve all courses from the database.
    """
    try:
        courses_collection = get_courses_collection()
        courses = list(courses_collection.find({}))
        for course in courses:
            course["_id"] = str(course["_id"])
        logger.info("All courses retrieved from database")
        return courses
    except PyMongoError as e:
        logger.error(f"Database error while retrieving all courses: {e}")
        raise


def get_course_by_id_service(course_id: str):
    """
    Service to retrieve a course by its ID.
    """
    try:
        courses_collection = get_courses_collection()
        course = courses_collection.find_one({"_id": course_id})
        if course:
            course["_id"] = str(course["_id"])
            logger.info(f"Course retrieved from database: {course_id}")
        return course
    except PyMongoError as e:
        logger.error(f"Database error while retrieving course with ID {course_id}: {e}")
        raise


def delete_course_service(course_id: str):
    """
    Service to delete a course by its ID.
    """
    try:
        courses_collection = get_courses_collection()
        result = courses_collection.delete_one({"_id": course_id})
        logger.info(f"Course deleted from database: {course_id}")
        return result.deleted_count
    except PyMongoError as e:
        logger.error(f"Database error while deleting course with ID {course_id}: {e}")
        raise
