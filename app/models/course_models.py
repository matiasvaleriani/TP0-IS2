from pydantic import BaseModel, Field
from typing import Dict, Any


class CourseCreate(BaseModel):
    """
    Represents the required fields to create a new course.
    """

    title: str
    description: str = Field(..., min_length=50, max_length=255)


class CourseResponse(BaseModel):
    """
    Defines the response structure for a successful course operation.
    """

    data: Dict[str, Any]
