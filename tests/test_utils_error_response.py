import pytest
from fastapi.responses import JSONResponse
from app.utils.error_response import create_rfc7807_error_response

def test_create_rfc7807_error_response():
    """
    Test the create_rfc7807_error_response function.
    """
    status_code = 404
    title = "Not Found"
    detail = "The requested resource was not found."
    instance = "/example/resource"

    response = create_rfc7807_error_response(status_code, title, detail, instance)

    assert isinstance(response, JSONResponse)
    assert response.status_code == status_code
    assert response.body == (
        b'{"type":"about:blank","title":"Not Found","status":404,'
        b'"detail":"The requested resource was not found.","instance":"/example/resource"}'
    )