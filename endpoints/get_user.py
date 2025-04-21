from fastapi import APIRouter, Depends, HTTPException
from security.dependencies import signature_verification
from models.user import UserInfo
from storage.data import db

router = APIRouter(dependencies=[Depends(signature_verification)])


@router.get("/get_user/{customer_id}", response_model=UserInfo)
def get_user(customer_id: str):
    customer_info = db.get(customer_id)

    if customer_info is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserInfo.model_validate(customer_info)
