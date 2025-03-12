from fastapi import APIRouter
from typing import Dict, Any
import uuid
import json
import os
from dotenv import load_dotenv
from .models import CourseResponse, CourseCreate
from .utils import create_error_response

# This is to to modularize our route definitions, improving code organization and maintainability. 
# This approach allows us to separate route logic into different files, making the codebase cleaner and easier to manage.
router = APIRouter()

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la aplicación
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DATA_FILE = os.getenv("DATA_FILE", "/app/data/courses.json")

# Asegurarse de que el archivo de datos exista
if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

@router.post("/courses", status_code=201, response_model=CourseResponse, responses={
    201: {
        "description": "Course created successfully",
        "content": {
            "application/json": {
                "example": {
                    "data": {
                        "id": 0,
                        "title": "string",
                        "description": "string"
                    }
                }
            }
        }
    },
    400: {
        "description": "Bad request error",
        "content": {
            "application/json": {
                "example": {
                    "type": "about:blank",
                    "title": "Bad Request",
                    "status": 400,
                    "detail": "Invalid input data",
                    "instance": "/courses"
                }
            }
        }
    }
})

def create_course(course: CourseCreate):
    if not isinstance(course.title, str) or not isinstance(course.description, str):
        return create_error_response(400, "Invalid input data", "/courses")
    
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    
    course_id = str(uuid.uuid4())
    new_course = {"id": course_id, "title": course.title, "description": course.description}
    courses[course_id] = new_course

    with open(DATA_FILE, 'w') as f:
        json.dump(courses, f)

    return {"data": new_course}

@router.get("/courses", response_model=Dict[str, Any], responses={
    200: {
        "description": "A list of courses",
        "content": {
            "application/json": {
                "example": {
                    "data": [
                        {
                            "id": 0,
                            "title": "string",
                            "description": "string"
                        }
                    ]
                }
            }
        }
    }
})
def get_courses():
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    return {"data": list(courses.values())}

@router.get("/courses/{id}", status_code=200, response_model=CourseResponse, responses={
    200: {
        "description": "Course created successfully",
        "content": {
            "application/json": {
                "example": {
                    "data": {
                        "id": 0,
                        "title": "string",
                        "description": "string"
                    }
                }
            }
        }
    },
    404: {
        "description": "Course not found",
        "content": {
            "application/json": {
                "example": {
                    "type": "about:blank",
                    "title": "Course Not Found",
                    "status": 404,
                    "detail": "The course with ID {id} was not found.",
                    "instance": "/courses/{id}"
                }
            }
        }
    },
    500: {
        "description": "Internal server error",
        "content": {
            "application/json": {
                "example": {
                    "type": "about:blank",
                    "title": "Internal Server Error",
                    "status": 500,
                    "detail": "An unexpected error occurred.",
                    "instance": "/courses/{id}"
                }
            }
        }
    }
})

def get_course(id: str):
    try:
        with open(DATA_FILE, 'r') as f:
            courses = json.load(f)
        
        course = courses.get(id)
        if not course:
            return create_error_response(404, "Course Not Found.", f"The course with ID {id} was not found.", f"/courses/{id}")
        return {"data": course}
    except Exception as e:
        return create_error_response(500, "Internal Server Error", "An unexpected error occurred.", f"/courses/{id}")

@router.delete("/courses/{id}", status_code=204, responses={
    204: {
        "description": "Course deleted successfully"
    },
    404: {
        "description": "Course not found",
        "content": {
            "application/json": {
                "example": {
                    "type": "about:blank",
                    "title": "Course Not Found",
                    "status": 404,
                    "detail": "The course with ID {id} was not found.",
                    "instance": "/courses/{id}}"
                }
            }
        }
    },
    500: {
        "description": "Internal server error",
        "content": {
            "application/json": {
                "example": {
                    "type": "about:blank",
                    "title": "Internal Server Error",
                    "status": 500,
                    "detail": "An unexpected error occurred.",
                    "instance": "/courses/{id}"
                }
            }
        }
    }
})

def delete_course(id: str):
    try:
        with open(DATA_FILE, 'r') as f:
            courses = json.load(f)
        
        course = courses.pop(id, None)
        if not course:
            return create_error_response(404, "Course Not Found.", f"The course with ID {id} was not found.", f"/courses/{id}")
        
        with open(DATA_FILE, 'w') as f:
            json.dump(courses, f)

        return {"message": "Course deleted successfully"}
    except Exception as e:
        return create_error_response(500, "Internal Server Error", "An unexpected error occurred.", f"/courses/{id}")