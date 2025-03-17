from fastapi.responses import JSONResponse


def create_rfc7807_error_response(
    status_code: int, title: str, detail: str, instance: str
):
    """
    Create an error response following the RFC 7807 format.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "type": "about:blank",
            "title": title,
            "status": status_code,
            "detail": detail,
            "instance": instance,
        },
    )
