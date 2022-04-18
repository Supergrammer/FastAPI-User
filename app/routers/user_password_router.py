from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.modules.auth_module import get_current_user

from app.schemas import user_schema, password_schema
from app.services import user_account_service, user_password_service
from app.http_exception import user_already_exist_exception, user_not_exist_exception


router = APIRouter(
    prefix="/password",
    tags=["user", "password"],
)

db = Depends(get_db)


@router.post("", response_model=user_schema.Response.UserReadDetail)
async def update_user_password(
    password: password_schema.Request.PasswordUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = db
):
    db_user = user_password_service.get_user_by_email(db=db, email=current_user)

    if not db_user:
        raise user_not_exist_exception

    return user_password_service.update_user_password(db=db, current_user=current_user, password=password)


@router.delete("", response_model=user_schema.Response.UserReadDetail)
async def delete_user(current_user: str = Depends(get_current_user), db: Session = db):
    db_user = user_account_service.get_user_by_email(db=db, email=current_user)

    if not db_user:
        raise user_not_exist_exception

    return user_account_service.delete_user(db=db, email=current_user)


@router.get("/all", response_model=list[user_schema.Response.UserRead])
def read_all_users(skip: int | None = None, limit: int | None = None, db: Session = db):
    return user_account_service.get_all_users(db=db, skip=skip, limit=limit)
