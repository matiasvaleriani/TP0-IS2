from pydantic import BaseModel
from typing import Dict, Any

class CourseCreate(BaseModel):
    """
    Represents the required fields to create a new course.
    """
    title: str
    description: str

class CourseResponse(BaseModel):
    """
    Defines the response structure for a successful course operation.
    """
    data: Dict[str, Any]

class ErrorResponse(BaseModel):
    """
    Represents an error response following the RFC 7807 format.
    """
    type: str
    title: str
    status: int
    detail: str
    instance: str
