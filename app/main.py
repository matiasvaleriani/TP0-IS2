from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import os
import json
from dotenv import load_dotenv
from app.errorHandlingMiddleware import ErrorHandlingMiddleware

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables de entorno con valores por defecto
HOST = os.getenv("HOST", "127.0.0.1")  # Si no se define, usa 127.0.0.1
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# Registrar el middleware
app.add_middleware(ErrorHandlingMiddleware)

# Ruta del archivo de datos
DATA_FILE = "/app/data/courses.json"

# Asegurarse de que el archivo de datos exista
if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

class CourseCreate(BaseModel):
    title: str
    description: str

@app.post("/courses/")
def create_course(course: CourseCreate):
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    
    course_id = str(uuid.uuid4())
    courses[course_id] = {"id": course_id, "title": course.title, "description": course.description}

    with open(DATA_FILE, 'w') as f:
        json.dump(courses, f)

    return {"message": "Course created", "data": courses[course_id]}

@app.get("/courses/")
def get_courses():
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    return {"data": list(courses.values())}

@app.get("/courses/{course_id}")
def get_course(course_id: str):
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    
    course = courses.get(course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with ID {} was not found.".format(course_id),
            headers={"X-Error": "Course not found"}
        )
    return {"data": course}

@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    with open(DATA_FILE, 'r') as f:
        courses = json.load(f)
    
    course = courses.pop(course_id, None)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with ID {} was not found.".format(course_id),
            headers={"X-Error": "Course not found"}
        )
    
    with open(DATA_FILE, 'w') as f:
        json.dump(courses, f)

    return {"message": "Course deleted successfully"}