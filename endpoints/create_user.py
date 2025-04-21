from fastapi import APIRouter, Depends, status
import uuid
from security.dependencies import signature_verification
from models.user import UserInfo, CreatedUser
from storage.data import db

router = APIRouter(dependencies=[Depends(signature_verification)])


@router.post("/create_user", response_model=CreatedUser, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserInfo):
    customer_id = str(uuid.uuid4())

    db.update({customer_id: payload.model_dump()})

    return CreatedUser(customer_id=customer_id)
