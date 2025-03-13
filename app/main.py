from app.routes import router
from app.utils import ensure_data_file_exists
from .utils import create_rfc7807_error_response
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError


app = FastAPI()


# Handler to catch HTTPExceptions and return a JSON response with the RFC7807 format
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return create_rfc7807_error_response(
        status_code=exc.status_code,
        title=exc.detail.split(".")[0],
        detail=exc.detail,
        instance=str(request.url),
    )


# Handler to catch general exceptions and return a JSON response with the RFC7807 format
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return create_rfc7807_error_response(
        status_code=500,
        title="Internal Server Error",
        detail="An unexpected error occurred.",
        instance=str(request.url),
    )


# Handler to catch RequestValidationErrors and return a JSON response with the RFC7807 format.
# For example, when a request is made with invalid data types.
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return create_rfc7807_error_response(
        status_code=422,
        title="Validation Error",
        detail=str(exc),
        instance=str(request.url),
    )


"""
Ensure the data file exists before the application starts.
"""
ensure_data_file_exists()

"""
Include the routes defined in the router.
"""
app.include_router(router)
