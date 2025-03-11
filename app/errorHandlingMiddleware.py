from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.errorResponse import ErrorResponse

class ErrorHandlingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            # Llamamos al siguiente middleware en la cadena
            await self.app(scope, receive, send)
        except RequestValidationError as e:
            # Capturar errores de validación
            error_detail = e.errors()[0]
            response = JSONResponse(
                status_code=400,  # Código HTTP 400 para error de validación
                content=ErrorResponse(
                    type="https://example.com/errors/validation-error",
                    title="Validation Error",
                    status=400,
                    detail=f"Field '{error_detail['loc'][1]}' should be of type {error_detail['type']}",
                    instance=str(scope['path'])  # Usamos el path de la URL como instance
                ).dict()
            )
            await response(scope, receive, send)
        except Exception as e:
            # Para otros errores, respondemos con un error interno del servidor
            response = JSONResponse(
                status_code=500,
                content=ErrorResponse(
                    type="https://example.com/errors/internal-server-error",
                    title="Internal Server Error",
                    status=500,
                    detail=str(e),
                    instance=str(scope['path'])
                ).dict()
            )
            await response(scope, receive, send)
