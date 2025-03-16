from app.routes import router
from app.utils import create_rfc7807_error_response
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from app.logging_config import get_logger

logger = get_logger()

app = FastAPI()


# Handler to catch HTTPExceptions and return a JSON response with the RFC7807 format
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    logger.error("HTTPException: {} - {}", exc.status_code, exc.detail)
    return create_rfc7807_error_response(
        status_code=exc.status_code,
        title=exc.detail.split(".")[0],
        detail=exc.detail,
        instance=str(request.url.path),
    )


# Handler to catch general exceptions and return a JSON response with the RFC7807 format
@app.exception_handler(Exception)
def general_exception_handler(request: Request, exc: Exception):
    logger.exception("An unexpected error occurred.")
    return create_rfc7807_error_response(
        status_code=500,
        title="Internal Server Error",
        detail="An unexpected error occurred.",
        instance=str(request.url.path),
    )


# Handler to catch RequestValidationErrors and return a JSON response with the RFC7807 format.
# For example, when a request is made with invalid data types.
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error("Validation Error: {}", exc)
    return create_rfc7807_error_response(
        status_code=422,
        title="Validation Error",
        detail=str(exc),
        instance=str(request.url.path),
    )


"""
Include the routes defined in the router.
"""
app.include_router(router)
