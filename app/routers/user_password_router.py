from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configurations.user_database import get_user_db
from app.modules.auth_module import get_current_user

from app.schemas import user_schema, password_schema
from app.services import user_password_service

from app.http_exception import credentials_exception


router = APIRouter(
    prefix="/password",
)

db = Depends(get_user_db)


@router.post("", response_model=user_schema.Response.UserReadDetail)
async def update_user_password(
    password: password_schema.Request.PasswordUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = user_password_service.get_user_by_email(
        db=db, email=current_user)

    if not db_user:
        raise credentials_exception

    return user_password_service.update_user_password(db=db, current_user=current_user, password=password)


@router.get("/expire-date")
async def get_password_expiration_date(
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = user_password_service.get_user_by_email(
        db=db, email=current_user)

    if not db_user:
        raise credentials_exception

    return user_password_service.get_expiration_date(db=db, current_user=current_user)
