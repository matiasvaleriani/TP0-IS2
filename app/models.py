from pydantic import BaseModel
from typing import Dict, Any

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