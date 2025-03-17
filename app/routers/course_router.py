from fastapi import APIRouter
from app.controllers.course_controller import (
    create_course_controller,
    get_all_courses_controller,
    get_course_by_id_controller,
    delete_course_controller,
)
from app.models.course_models import CourseCreate, CourseResponse
from typing import Dict, Any

router = APIRouter()


@router.post("/courses", status_code=201, response_model=CourseResponse)
def create_course(course: CourseCreate):
    return {"data": create_course_controller(course.title, course.description)}


@router.get("/courses", response_model=Dict[str, Any])
def get_courses():
    return {"data": get_all_courses_controller()}


@router.get("/courses/{id}", status_code=200, response_model=CourseResponse)
def get_course(id: str):
    return {"data": get_course_by_id_controller(id)}


@router.delete("/courses/{id}", status_code=204)
def delete_course(id: str):
    delete_course_controller(id)
    return {"message": "Course deleted successfully"}