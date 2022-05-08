from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configurations.user_database import get_user_db
from app.modules.auth_module import get_current_user

from app.schemas import user_schema
from app.services import user_service
from app.services.common import get_user_by_email

from app.http_exception import user_already_exist_exception, user_not_exist_exception, credentials_exception


router = APIRouter(
    prefix="/users",
    tags=["user"],
)

db = Depends(get_user_db)


@router.post("", response_model=user_schema.Response.UserReadDetail)
def create_user(
    user: user_schema.Request.UserCreate,
    db: Session = db
):
    db_user = get_user_by_email(db=db, email=user.email)

    if db_user:
        raise user_already_exist_exception

    return user_service.create_user(db=db, user=user)


@router.get("", response_model=user_schema.Response.UserRead)
async def read_user(
    email: str,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = get_user_by_email(db=db, email=email)

    if not db_user:
        raise user_not_exist_exception

    return db_user


@router.put("", response_model=user_schema.Response.UserReadDetail)
async def update_user(
    user: user_schema.Request.UserUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_current_user = get_user_by_email(db=db, email=current_user)

    if not db_current_user:
        raise credentials_exception

    return user_service.update_user(db=db, current_user=current_user, user=user)


@router.delete("", response_model=user_schema.Response.UserReadDetail)
async def delete_user(
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_current_user = get_user_by_email(db=db, email=current_user)

    if not db_current_user:
        raise credentials_exception

    return user_service.delete_user(db=db, current_user=current_user)


@router.get("/check")
def check_user_email(
    email: str,
    db: Session = db
):
    db_user = get_user_by_email(db=db, email=email)

    return {"is_exist": bool(db_user)}


@router.get("/me", response_model=user_schema.Response.UserReadDetail)
async def read_user_me(
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_current_user = get_user_by_email(db=db, email=current_user)

    if not db_current_user:
        raise credentials_exception

    return db_current_user


@router.get("/me/active", response_model=user_schema.Response.UserReadDetail)
async def read_user_me_active(
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_current_user = get_user_by_email(db=db, email=current_user)

    if not db_current_user or not db_current_user.is_active:
        raise credentials_exception

    return db_current_user
