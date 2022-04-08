from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.services import user_account

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("")
async def create_user(db: Session = Depends(get_db)):
    return user_account.create_user(db=db, email="eee")

@router.get("")
async def read_user():
    return {"123": 123123}

@router.put("")
async def update_user():
    return {}

@router.delete("")
async def delete_user():
    return {}