from fastapi import Request, HTTPException, status
from models.error_response import ErrorResponse
from settings.config import settings


def signature_verification(request: Request):
    x_api_key = request.headers.get("x-api-key")
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorResponse(message="Missing x-api-key header", code=101).dict()
        )

    if x_api_key != settings.x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorResponse(message="Invalid x-api-key header", code=101).dict()
        )

    return True
