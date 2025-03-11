from fastapi import FastAPI
import uuid
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables de entorno con valores por defecto
HOST = os.getenv("HOST", "127.0.0.1")  # Si no se define, usa 127.0.0.1
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# "Base de datos" en memoria
courses = {}

@app.post("/courses/")
def create_course(description: str):
    course_id = str(uuid.uuid4())
    courses[course_id] = {"id": course_id, "description": description}
    return {"message": "Course created", "data": courses[course_id]}

@app.get("/courses/")
def get_courses():
    return {"data": list(courses.values())}

@app.get("/courses/{course_id}")
def get_course(course_id: str):
    course = courses.get(course_id)
    if not course:
        return {"error": "Course not found"}
    return {"data": course}
