from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.services import user_account_service

from app.schemas import user_schema

from app.modules.auth_module import get_current_user

from app.http_exception import user_already_exist_exception, user_not_exist_exception


router = APIRouter(
    prefix="/users",
    tags=["user"],
)

db = Depends(get_db)


@router.post("", response_model=user_schema.Response.UserReadDetail)
def create_user(
    user: user_schema.Request.UserCreate,
    db: Session = db
):
    db_user = user_account_service.get_user_by_email(db=db, email=user.email)

    if db_user:
        raise user_already_exist_exception

    return user_account_service.create_user(db=db, user=user)


@router.get("", response_model=user_schema.Response.UserRead)
async def read_user(
    email: str,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = user_account_service.get_user_by_email(db=db, email=email)

    if not db_user:
        raise user_not_exist_exception

    return db_user


@router.put("", response_model=user_schema.Response.UserReadDetail)
async def update_user(
    user: user_schema.Request.UserUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = user_account_service.get_user_by_email(db=db, email=current_user)

    if not db_user:
        raise user_not_exist_exception

    return user_account_service.update_user(db=db, email=current_user, user=user)


@router.delete("", response_model=user_schema.Response.UserReadDetail)
async def delete_user(current_user: str = Depends(get_current_user), db: Session = db):
    db_user = user_account_service.get_user_by_email(db=db, email=current_user)

    if not db_user:
        raise user_not_exist_exception

    return user_account_service.delete_user(db=db, email=current_user)


@router.get("/all", response_model=list[user_schema.Response.UserRead])
def read_all_users(skip: int | None = None, limit: int | None = None, db: Session = db):
    return user_account_service.get_all_users(db=db, skip=skip, limit=limit)
