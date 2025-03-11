from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any
from app.errorResponse import ErrorResponse
import uuid
import os
import json
from dotenv import load_dotenv
from fastapi import Body

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la aplicación
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# Ruta del archivo de datos
DATA_FILE = "/app/data/courses.json"

# Asegurarse de que el archivo de datos exista
if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

# Modelos para la creación de un curso y las respuestas
class CourseCreate(BaseModel):
    title: str
    description: str

class CourseResponse(BaseModel):
    data: Dict[str, Any]

class ErrorResponse(BaseModel):
    type: str
    title: str
    status: int
    detail: str
    instance: str

# Función para crear respuestas de error en formato RFC 7807
def create_error_response(status_code: int, detail: str, instance: str):
    return JSONResponse(
        status_code=status_code,
        content={
            "type": "about:blank",
            "title": detail,
            "status": status_code,
            "detail": detail,
            "instance": instance
        }
    )

# Ruta para crear un curso
@app.post("/courses", status_code=201, response_model=CourseResponse, responses={
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
def create_course(course: Dict[str, Any] = Body(..., example={"title": "string", "description": "string"})):
    if not isinstance(course.get("title"), str) or not isinstance(course.get("description"), str):
        return create_error_response(400, "Invalid input data", "/courses")
    
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    
    course_id = str(uuid.uuid4())
    new_course = {"id": course_id, "title": course["title"], "description": course["description"]}
    courses[course_id] = new_course

    with open(DATA_FILE, 'w') as f:
        json.dump(courses, f)

    return {"data": new_course}

# Ruta para obtener todos los cursos
@app.get("/courses", response_model=Dict[str, Any], responses={
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

# Ruta para obtener un curso por ID
@app.get("/courses/{id}", status_code= 200, response_model=CourseResponse, responses={
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
                    "detail": "The course with ID 12345 was not found.",
                    "instance": "/courses/12345"
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
            return create_error_response(404, f"The course with ID {id} was not found.", f"/courses/{id}")
        return {"data": course}
    except Exception as e:
        return create_error_response(500, "An unexpected error occurred.", f"/courses/{id}")

# Ruta para eliminar un curso por ID
@app.delete("/courses/{id}", status_code = 204, responses={
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
                    "detail": "The course with ID 12345 was not found.",
                    "instance": "/courses/12345"
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
            return create_error_response(404, f"The course with ID {id} was not found.", f"/courses/{id}")
        
        with open(DATA_FILE, 'w') as f:
            json.dump(courses, f)

        return {"message": "Course deleted successfully"}
    except Exception as e:
        return create_error_response(500, "An unexpected error occurred.", f"/courses/{id}")