from fastapi import APIRouter, Depends, HTTPException, status
from security.dependencies import signature_verification
from models.user import UserInfo
from models.error_response import ErrorResponse
from storage.data import db

router = APIRouter(dependencies=[Depends(signature_verification)])


@router.get("/get_user/{customer_id}", response_model=UserInfo)
def get_user(customer_id: str):
    customer_info = db.get(customer_id)

    if customer_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(message="User not found", error_code=103).dict()
        )

    return UserInfo.model_validate(customer_info)
