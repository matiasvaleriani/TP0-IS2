from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    Represents an error response following the RFC 7807 format.
    """
    type: str
    title: str
    status: int
    detail: str
    instance: str