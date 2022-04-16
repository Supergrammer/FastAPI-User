from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.services import user_account_service

from app.schemas import user_schema

router = APIRouter(
    prefix="/password",
    tags=["user", "password"],
)

db = Depends(get_db)


@router.post("", response_model=user_schema.User)
async def create_user(user: user_schema.UserCreate, db: Session = db):
    db_user = user_account_service.get_user(db=db, email=user.email)
    
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail already exists."
        )

    return user_account_service.create_user(db=db, user=user)


@router.get("", response_model=user_schema.User)
async def read_user(email: str, db: Session = db):
    db_user = user_account_service.get_user(db=db, email=email)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail does not exist."
        )

    return db_user


@router.put("", response_model=user_schema.User)
async def update_user(user: user_schema.UserCreate, db: Session = db):
    db_user = user_account_service.get_user(db=db, email=user.email)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail does not exist."
        )

    return user_account_service.update_user(db=db, user=user)


@router.delete("", response_model=user_schema.User)
async def delete_user(email: str, db: Session = db):
    db_user = user_account_service.get_user(db=db, email=email)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail does not exist."
        )

    return user_account_service.delete_user(db=db, email=email)


@router.get("/all", response_model=list[user_schema.User])
async def read_all_users(skip: int | None = None, limit: int | None = None, db: Session = db):
    return user_account_service.get_all_users(db=db, skip=skip, limit=limit)
