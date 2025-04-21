from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    error_code: int
