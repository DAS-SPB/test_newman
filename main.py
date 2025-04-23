from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from endpoints import create_user, get_user
from models.error_response import ErrorResponse

PREFIX = "/simple_app"

simple_app = FastAPI()


@simple_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponse(
            message="Invalid request",
            error_code=102
        ).model_dump()
    )


@simple_app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    detail = exc.detail
    if isinstance(detail, dict):
        message = detail.get("message", str(detail))
        error_code = detail.get("error_code", exc.status_code)
    else:
        message = str(detail)
        error_code = exc.status_code

    payload = ErrorResponse(message=message, error_code=error_code).model_dump()

    return JSONResponse(status_code=exc.status_code, content=payload)


simple_app.include_router(router=create_user.router, prefix=PREFIX)
simple_app.include_router(router=get_user.router, prefix=PREFIX)


@simple_app.get(f"{PREFIX}/health")
def healthcheck():
    return {"status": "OK"}
